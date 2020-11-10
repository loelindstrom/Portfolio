package loelin8.gui;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.swing.*;

import loelin8.banksystem.*;

/**
 * A GUI for a bank system (specified in the folder "banksystem").
 * All the functionality of the bank system can be reached through 
 * this graphical interface.
 * 
 * This class inherits from the javax.swing.JFrame class
 * and is therefore the window containing the whole
 * GUI.
 * 
 * The GUI consists of two main panels divided into subparts:
 * 
 *  |- JPanel customerListPanel
 *  |     (a panel displaying all the customers of the bank) 
 *  |
 *  |- JPanel panelForTabs
 *  |     (a panel holding the below panels in tabs)
 *      |
 *      |- JPanel customerInfoPanel
 *      |     (info/actions about a selected customer and attached accounts)
 *      |
 *      |- JPanel addCustomerPanel
 *      |     (menu for adding new customers)
 *      |
 *      |- JPanel exportCustomerPanel
 *      |     (menu for exporting customer-info to external files)
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class BankGUI extends JFrame
{   
    /**
     * To start and run the application.
     */
    public static void main(String[] args)
    {
        BankGUI win = new BankGUI();
        win.setVisible(true);
    }
    
    // The window/frame settings:
    private static final int FWIDTH = 820;
    private static final int FHEIGHT = 600;
    
    // The underlying bank system:
    private BankLogic bankLogic;
    
    // Components for creating a menubar:
    JMenuBar menuBar;
    JMenu menu;
    JMenuItem[] menuItems;
    
    // Component holding a list with all the customers:
    private CustomerListPanel customerListPanel;
    
    // Components for the tabs:
    private JPanel panelForTabs;
    private JTabbedPane tabPane;
    private String[] tabNames = {"Kundinfo", "Lägg till", "Exportera"};
    private String[] tabTips = {"Se och hantera kunds konton.", 
                        "Lägg till nya kunder i systemet.",
                        "Exportera kunder till extern fil."};
    
    // Components for the interfaces of handling the customers
    // Which are added to the "panelForTabs":
    private JPanel customerInfoPanel;
    private JPanel addCustomerPanel;
    private JPanel exportCustomerPanel;
    
    /**
     * Instantiates all the parts of the GUI
     */
    public BankGUI()
    {   
        // Creates the window and sets its title:
        super("Ultimate Bank");
        
        // Sets the window-preferences:
        this.setWindowPreferences();
        
        // Creates an instance of the underlaying Logic 
        // which is the basis of the GUI
        bankLogic = new BankLogic();
        
        // Adds some place holder-customers and creates transactions 
        // history for the first added customer's first account:
        bankLogic.createCustomer("Hans", "Holmer", "4205267823");
        bankLogic.createCreditAccount("4205267823");
        bankLogic.deposit("4205267823", 1001, 10000);
        bankLogic.withdraw("4205267823", 1001, 400.32);
        for (int i = 0; i < 5; i++)
        {
            bankLogic.createSavingsAccount("4205267823");
        }
        bankLogic.createCustomer("Sanh", "Remloh", "2305267822");
        bankLogic.createSavingsAccount("2305267822");
        bankLogic.createCustomer("Andrea", "Hermansson", "8205267822");
        bankLogic.createCreditAccount("8205267822");
        
        // Creating the menuBar:
        createMenuBar();
        
        // Creating the panel holding the list of all the customers.
        // The underlying bankLogic and this parent-window is sent with:
        customerListPanel = new CustomerListPanel(this, bankLogic);
        
        // Creates the three JPanel-components which consitutes the interface
        // to handle the customers. They are later placed in tabs.
        // The underlying bankLogic and this parent-window is sent with them:
        customerInfoPanel = new CustomerInfoPanel(this, bankLogic);
        addCustomerPanel = new AddCustomerPanel(this, bankLogic);
        exportCustomerPanel = new ExportCustomerPanel(this, bankLogic);
        
        // Creates the tabs and puts the interfacing panels
        // inside of them:
        panelForTabs = new JPanel();
        tabPane = new JTabbedPane();
        JPanel[] tabPanels = {customerInfoPanel, addCustomerPanel, exportCustomerPanel};
        for (int i = 0; i < tabPanels.length; i++)
        {
            tabPane.addTab(tabNames[i], null, tabPanels[i], tabTips[i]);
        }
        panelForTabs.add(tabPane);
        
        // Sets the layout for the JPanel components:
        this.setLayout(new BorderLayout());
        this.add(customerListPanel, BorderLayout.WEST);
        this.add(tabPane);
    }
    
    private void createMenuBar()
    {
        menuBar = new JMenuBar();
        menu = new JMenu("Meny");
        JMenu view = new JMenu("Vy");
        menuItems = new JMenuItem[tabNames.length];
        
        MenuListener menuListener = new MenuListener();
        
        for (int i = 0; i < tabNames.length; i++)
        {
            menuItems[i] = new JMenuItem(tabNames[i]);
            menuItems[i].addActionListener(menuListener);
            view.add(menuItems[i]);
        }
        menuItems[0].setEnabled(false);
        menu.add(view);
        
        menu.addSeparator();
        JMenuItem exitItem = new JMenuItem("Avsluta");
        exitItem.addActionListener(menuListener);
        menu.add(exitItem);
        
        menuBar.add(menu);
        this.setJMenuBar(menuBar);
        
    }
    /**
     * Listens to when the items in the
     * menu are clicked and switches focus 
     * to the tab chosen in the menu.
     * 
     * Or exiting the program if the exit-choice
     * is chosen.
     * @author Loe Lindström, loelin-8
     *
     */
    class MenuListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e)
        {
            String itemClicked = ((JMenuItem)e.getSource()).getText();
            int index = tabNames.length;
            for (int i = 0; i < tabNames.length; i++)
            {
                menuItems[i].setEnabled(true);
                if (itemClicked.equals(tabNames[i]))
                    index = i;
            }
            if (index == tabNames.length)
                System.exit(EXIT_ON_CLOSE);
            else
            {
                tabPane.setSelectedIndex(index);
                menuItems[index].setEnabled(false);
            }
        }
        
    }

    /**
     * Sets the width and height of the window
     * and makes it possible to to close the window
     */
    private void setWindowPreferences()
    {
        this.setSize(FWIDTH, FHEIGHT);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
    
    /**
     * Updates the JPanel "customerList" with the latest added customer
     */
    public void updateCustomerList()
    {
        customerListPanel.updateCustomerList();
    }
    
    /**
     * Updates the customer info label
     * within the JPanel "customerInfoPanel"
     * based on which customer is selected in the "customerListPanel".
     */
    public void updateCustomerInfoLabel(String name, String persNo)
    {
        ((CustomerInfoPanel)customerInfoPanel).updateCustomerInfoLabel(name, persNo);
    }
    
    /**
     * Makes the graphical account-list within 
     * the JPanel "customerInfoPanel" empty.
     */
    public void clearAccountList()
    {
        ((CustomerInfoPanel)customerInfoPanel).clearAccountList();
    }
    
    /**
     * Updates the account list within the JPanel "customerInfoPanel"
     * based on which customer is selected 
     * in the JPanel CustomerListPanel.
     * @param accounts
     */
    public void updateAccountList(ArrayList<String> accounts)
    {
        ((CustomerInfoPanel)customerInfoPanel).updateAccountList(accounts);
    }
    
    /**
     * Used to check if the input is correct.
     * Used both in the JPanel "AddCustomerPanel"
     * and JPanel "CustomerInfoPanel".
     * Returns a String with what in the input is wrong
     * or an empty String if nothing is wrong.
     * 
     * @param fname String
     * @param surname String
     * @param persNo String
     * @return String checkMessage
     */
    public static String checkInput(String fname, String surname, String persNo)
    {
        String checkMessage = "";
        if (fname.isBlank())
            checkMessage += "Förnamn saknas\n";
        if (surname.isBlank())
            checkMessage += "Efternamn saknas\n";
        if (persNo.isBlank())
            checkMessage += "Personnummer saknas\n";
        if (persNo.length() != 10)
            checkMessage += "Personnummer har fel längd\n";
        else
        {
            Pattern month = Pattern.compile("^(1[0-2]|0[1-9])$");
            Matcher monthMatcher = month.matcher(persNo.substring(2, 4));
            Pattern day = Pattern.compile("0[1-9]|[12][0-9]|3[01]");
            Matcher dayMatcher = day.matcher(persNo.substring(4, 6));
            if (!monthMatcher.find())
                checkMessage += "Personnummer har ogiltig månad\n";
            if (!dayMatcher.find())
                checkMessage += "Personnummer har ogiltig dag\n";
        }
        return checkMessage;
    }
}
