package loelin8.gui;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import loelin8.banksystem.BankLogic;

/**
 * A JPanel inheriting class which displays
 * a list with all the customers of a bank via
 * the underlying system logic "bankLogic".
 * 
 * This panel is used by its "parent"- window
 * - and BankGUI-instance.
 * 
 * There are also actions that can be performed 
 * through on the list via buttons:
 *    - Select all customers in the list
 *    - Sort the list
 *    - Remove customer(s) selected in the list.
 *  
 * @author Loe Lindström, loelin-8
 *
 */
public class CustomerListPanel extends JPanel
{
    // Parent window:
    private BankGUI parent;
    
    // Underlying logic:
    private BankLogic bankLogic;    
    
    // List containing the bank's customers:
    private ArrayList<String> customers;
    private DefaultListModel<String> customerListItems;
    private JList<String> customerList;
    
    // Buttons:
    String[] buttonNames = {"Välj alla", "Sortera", "Ta bort"};
    JButton[] buttons;
    
    public CustomerListPanel(BankGUI parent, BankLogic bankLogic)
    {
        this.parent = parent;
        
        this.bankLogic = bankLogic;
        
        this.setLayout(new BorderLayout());
        this.setPreferredSize(new Dimension(350, 300));
        
        // Create the content:
        createTitledBorder("Kunder");
        createCustomerList();
        createButtons();
        
    }
    
    /**
     * Creates a border around the panel with a title up in the left corner.
     * @param titleName String
     */
    private void createTitledBorder(String titleName)
    {
        TitledBorder title = BorderFactory.createTitledBorder(titleName);
        this.setBorder(title);
        
    }
    
    /**
     * Creates the list containing all the customers of
     * the bank. Dimension is specified here. ListSelectionListener is
     * added ("CustomerListListener").
     */
    private void createCustomerList()
    {
        customers = bankLogic.getAllCustomers();
        customerListItems = new DefaultListModel<String>();
        customerListItems.addAll(customers);
        customerList = new JList<String>(customerListItems);
        customerList.addListSelectionListener(new CustomerListListener());
        JScrollPane customerScrollPane = new JScrollPane(customerList);
        this.add(customerScrollPane, BorderLayout.CENTER);
    }
    /**
     * An inner class which listens to when customers are selected
     * in the customerList (outer class) and displays the customerInfo
     * in the JPanel customerInfoPanel (Situated in parent class).
     * @author Loe Lindström, loelin-8
     *
     */
    class CustomerListListener implements ListSelectionListener {

        @Override
        public void valueChanged(ListSelectionEvent e)
        {
            if (e.getValueIsAdjusting() == false && !customerList.isSelectionEmpty()) {
                String selected = customerList.getSelectedValue();
                String name = selected.substring(11);
                String persNo = selected.substring(0, 10);
                
                ArrayList<String> accounts = bankLogic.getAccountsShortInfo(persNo);
                
                parent.updateCustomerInfoLabel(name, persNo);
                parent.updateAccountList(accounts);
            }
            
        }
        
    }
    
    /**
     * Creates the buttons specified in the private field "buttonNames".
     * and adds an instance of the "ListButtonListener"-class to them.
     */
    private void createButtons()
    {   
        JPanel buttonPanel = new JPanel();
        buttons = new JButton[buttonNames.length];
        ActionListener listener = new ListButtonListener();
        for (int i = 0; i < buttonNames.length; i++)
        {
            buttons[i] = new JButton(buttonNames[i]);
            buttons[i].addActionListener(listener);
            buttonPanel.add(buttons[i]);
        }
        this.add(buttonPanel, BorderLayout.SOUTH);
    }
    
    /**
     * A class which listens to the buttons in the outer
     * class.
     * @author Loe Lindström, loelin-8
     *
     */
    class ListButtonListener implements ActionListener
    {
        private int sortCounter = 0;

        @Override
        /**
         * button 0 = select all customers
         * button 1 = sort customer list
         * button 2 = delete selected customers
         */
        public void actionPerformed(ActionEvent e)
        {
            String buttonName = ((JButton)e.getSource()).getText();
            
            // Selects all customers in the list
            if (buttonName.equals(buttonNames[0])) {
                int end = customerList.getModel().getSize() - 1;
                customerList.setSelectionInterval(0, end);
                
            }
            // Sorts customerList:
            else if (buttonName.equals(buttonNames[1])) {
                if (sortCounter == 0)
                {
                    Collections.sort(customers);
                    sortCounter++;
                }
                else
                {
                    Collections.sort(customers, Collections.reverseOrder());
                    sortCounter = 0;
                }
                
                customerListItems.clear();
                customerListItems.addAll(customers);
                customerList.setModel(customerListItems);
                
            }
            // Removes selected customers
            else if (buttonName.equals(buttonNames[2])) {
                
                // Do nothing if no customer is selected:
                if (customerList.isSelectionEmpty())
                    return;
                
                // Ask user to confirm removal of selected customers:
                String confirmDeleteCustomerMsg = "Är du säker på att du vill ta bort vald(a) kund(er)?";
                String[] optionsConfirmDeleteCustomer = {"Nej", "Ja"};
                int confirmCustomerDelete = JOptionPane.showOptionDialog(parent, 
                                             confirmDeleteCustomerMsg, 
                                             "Ta bort valda kunder", 
                                             0, 
                                             JOptionPane.WARNING_MESSAGE, 
                                             null, 
                                             optionsConfirmDeleteCustomer, 
                                             0);
                
                // If customer confirms customers are deleted:
                if (confirmCustomerDelete == 1)
                {
                    String deletionMessage = deleteCustomers();
                    
                    // The deleted customers are displayed in a message dialog
                    JPanel deletionPanel = new JPanel(new BorderLayout());
                    JLabel deletionInfoLabel = new JLabel("Information om borttagna kunder:");
                    JTextArea deletionText = new JTextArea(deletionMessage);
                    JScrollPane deletionTextScroll = new JScrollPane(deletionText);
                    deletionTextScroll.setPreferredSize(new Dimension(300, 450));
                    deletionPanel.add(deletionInfoLabel, BorderLayout.NORTH);
                    deletionPanel.add(deletionTextScroll, BorderLayout.CENTER);
                    
                    
                    JOptionPane.showMessageDialog(parent, deletionPanel, "Valda kunder borttagna", JOptionPane.INFORMATION_MESSAGE);
                    
                    // Update the customer list.
                    // Happens after user has pressed ok in previos message dialog.
                    // This is so the user can compare the selected customers
                    // to the deleted customers.
                    updateCustomerList();
                    parent.updateCustomerInfoLabel("", "");
                    parent.clearAccountList();
                }
            }
        }       
    }
    
    /**
     * Updates the graphical customer list
     * so it concurs with the underlying bank logic list.
     */
    public void updateCustomerList()
    {
        customers = bankLogic.getAllCustomers();
        customerListItems.clear();
        customerListItems.addAll(customers);
        customerList.setModel(customerListItems);
    }
    
    /**
     * Deletes the customers that are selected
     * in the customer list and creates a String
     * with information about the deleted customers
     * and their accounts.
     * 
     * @return String deletionMessage
     */
    private String deleteCustomers()
    {
        List<String> customersToDelete = customerList.getSelectedValuesList();
        
        // Save information about deleted customers and their accounts:
        ArrayList<ArrayList<String>> deletedCustomersInfo = new ArrayList<>();
        for (String customerString : customersToDelete)
        {
            String persNo = customerString.substring(0, 10);
            deletedCustomersInfo.add(bankLogic.deleteCustomer(persNo));
        }
        
        // Inform user about successful removal and display information about
        // each deleted customer:
        String deletionMessage = "";
        
        for (ArrayList<String> customer : deletedCustomersInfo)
        {   
            // If customer don't have accounts only customer persNo 
            // and name is displayed.
            // Else each account is displayed.
            if (customer.size() == 1)
                deletionMessage += String.format("%s%n  Inga konton existerande vid borttagning.\n",
                        customer.get(0));
            else
            {
                deletionMessage += String.format("%s%n", customer.get(0));
                for (int i = 1; i < customer.size(); i++)
                    deletionMessage += String.format("  %s%n", customer.get(i));
            }
            deletionMessage += "\n";
        }
        return deletionMessage;
    }
}
