package loelin8.gui;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import loelin8.banksystem.BankLogic;

/**
 * A JPanel inheriting class which is used by its
 * "parent" - a BankGUI instance.
 * 
 * This JPanel contains info about customers in a bank 
 * specified through an underlying logic which is found
 * in the field BankLogic bankLogic.
 * 
 * The info about the customer is the following:
 *   - Name, personal number
 *   - Accounts attached to the customer
 *   - Info about respective account
 *  
 * The actions that can be performed in this panel are:
 *   - Change customer's name
 *   - Add/delete accounts
 *   - Deposit/withdraw money
 *   - View account-transactions
 *    
 * @author Loe Lindström, loelin-8
 *
 */
public class CustomerInfoPanel extends JPanel
{
    // Parent window:
    private BankGUI parent;    
    
    // Underlying logic:
    private BankLogic bankLogic;
    
    // To keep track of the current customer and account being displayed:
    private String fname;
    private String surname;
    private String customerPersNo;
    private int customerAccountId;
    
    // Customer info-label and edit button:
    private JTextArea customerInfo;
    private JButton editButton;
    
    
    // Account info-panel with its buttons, list and labels:
    private JPanel accountPanel;
    
    // Buttons for creating new or deleting accounts:
    private String[] addCloseButtonNames = {"Lägg till konto", "Ta bort konto"};
    private JButton[] addCloseButtons;
    
    // The list showing a customers accounts, where the user can select one of them:
    private DefaultListModel<String> accountListItems;
    private JList<String> accountList;
    
    // The components displaying more detailed information about the selected account
    private JTextArea accountInfoLeft;
    private JTextArea accountInfoRight;
    
    // Buttons for deposit, withdraw or see transactions of the selected account
    private String[] accountActionButtonNames = {"Sätt in", "Ta ut", "Se transaktioner"};
    private JButton[] accountActionButtons;
    
    public CustomerInfoPanel(BankGUI parent, BankLogic bankLogic)
    {
        this.parent = parent;
        
        this.bankLogic = bankLogic;
        
        createTitledBorder("Info");
        createCustomerInfoAndEdit();
        createAccountPanel("Konton");
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
     * Creates the topmost part of this panel
     * containing info about a selected customer
     * and a button to edit that persons name.
     */
    private void createCustomerInfoAndEdit()
    {
        JPanel topPanel = new JPanel();
        
        customerInfo = new JTextArea();
        customerInfo.setEditable(false);
        customerInfo.setPreferredSize(new Dimension(300, 50));
        customerInfo.setBackground(this.getBackground());
        topPanel.add(customerInfo);
        
        editButton = new JButton("Ändra");
        editButton.addActionListener(new EditButtonListener());
        topPanel.add(editButton);
        
        topPanel.setPreferredSize(new Dimension(400, 60));
        this.add(topPanel);
    }
    /**
     * Class that listens to the edit button
     * and opens a form-dialouge window if it is pressed.
     * 
     * @author Loe Lindström, loelin-8
     */
    class EditButtonListener implements ActionListener
    {
        @Override
        public void actionPerformed(ActionEvent e)
        {   
            // Only show dialog if a customer is selected:
            if (!customerInfo.getText().isEmpty())
            {
                // Creating the dialog form:
                JPanel editCustomerNamePanel = new JPanel();
                JLabel fnameLabel = new JLabel("Förnamn:");
                JTextField  fnameField = new JTextField(15);
                JLabel surnameLabel = new JLabel("Efternamn:");
                JTextField  surnameField = new JTextField(15);
                JTextArea errorSuccessLabel = new JTextArea("");
                errorSuccessLabel.setEditable(false);
                errorSuccessLabel.setBackground(parent.getBackground());
                errorSuccessLabel.setForeground(Color.red);
                errorSuccessLabel.setFocusable(false);
                editCustomerNamePanel.add(fnameLabel);
                editCustomerNamePanel.add(fnameField);
                editCustomerNamePanel.add(surnameLabel);
                editCustomerNamePanel.add(surnameField);
                editCustomerNamePanel.add(errorSuccessLabel);
                editCustomerNamePanel.setPreferredSize(new Dimension(250, 200));
                
                // Dialog-options:
                String[] optionsEditCustomer = {"Avbryt", "Spara"};
                
                // Show dialog:
                int edit = JOptionPane.showOptionDialog(parent, 
                                                        editCustomerNamePanel, 
                                                        "Ändra namn", 
                                                        0, 
                                                        JOptionPane.PLAIN_MESSAGE, 
                                                        null, 
                                                        optionsEditCustomer, 
                                                        null);
                
                // If user confirms edit
                // the input is checked and if 
                // it's ok the customer's name is updated.
                if (edit == 1)
                {
                    fname = fnameField.getText();
                    surname = surnameField.getText();
                    String checkMessage = BankGUI.checkInput(fname, surname, customerPersNo);
                    while (!checkMessage.isEmpty() && edit == 1)
                    {
                        errorSuccessLabel.setText(checkMessage);
                        edit = JOptionPane.showOptionDialog(parent, 
                                editCustomerNamePanel, 
                                "Ändra namn", 
                                0, 
                                JOptionPane.PLAIN_MESSAGE, 
                                null, 
                                optionsEditCustomer, 
                                null);
                        fname = fnameField.getText();
                        surname = surnameField.getText();
                        checkMessage = BankGUI.checkInput(fname, surname, customerPersNo);
                    }
                    bankLogic.changeCustomerName(fname, surname, customerPersNo);
                    updateCustomerInfoLabel(fname + " " + surname, customerPersNo);
                    parent.updateCustomerList();
                }
            }
        }
        
    }
    
    /**
     * Creates the titled-framed panel
     * containing the customers accounts, 
     * info about a selected account and
     * buttons to do actions on the accounts.
     */
    private void createAccountPanel(String titleName)
    {   
        // Creates the panel and its titled border:
        accountPanel = new JPanel();
        TitledBorder title = BorderFactory.createTitledBorder(titleName);
        accountPanel.setBorder(title);
        accountPanel.setPreferredSize(new Dimension(430, 400));
        
        // Creates the components residing inside the JPanel:
        createAddCloseButtons();
        createAccountList();
        createAccountInfo();
        createAccountActionButtons();
        
        this.add(accountPanel);
        
    }


    /**
     * Creates the buttons for adding a new account
     * or closing an existing account. 
     */
    private void createAddCloseButtons()
    {
        ActionListener addCloseListener = new AddCloseAccountListener();
        addCloseButtons = new JButton[addCloseButtonNames.length];
        for (int i = 0; i < addCloseButtonNames.length; i++)
        {
            addCloseButtons[i] = new JButton(addCloseButtonNames[i]);
            addCloseButtons[i].addActionListener(addCloseListener);
            accountPanel.add(addCloseButtons[i]);
        }
        
    }
    /**
     * Inner class that listens to the add and close account buttons.
     * Opens RadioButton-dialog when creating to let the user choose which
     * type of account to open.
     * Opens confirm dialog if user press delete button.
     * @author Loe Lindström, loelin-8
     *
     */
    class AddCloseAccountListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e)
        {
            String buttonName = ((JButton)e.getSource()).getText();
            
            // Add account-button
            if (buttonName.equals(addCloseButtonNames[0]) && !customerInfo.getText().isEmpty()) 
            {
                JPanel addAccountFormPanel = new JPanel();
                
                JLabel infoAddAccountForm = new JLabel("Välj kontotyp:");
                addAccountFormPanel.add(infoAddAccountForm);
                
                ButtonGroup optionsGroup = new ButtonGroup();
                String[] accountTypes = {"Sparkonto", "Kreditkonto"};
                JRadioButton[] accountTypeRButtons = new JRadioButton[accountTypes.length];
                for (int i = 0; i < accountTypes.length; i++)
                {
                    accountTypeRButtons[i] = new JRadioButton(accountTypes[i]);
                    optionsGroup.add(accountTypeRButtons[i]);
                    addAccountFormPanel.add(accountTypeRButtons[i]);
                }
                accountTypeRButtons[0].setSelected(true);
                
                String[] optionsAddAccountForm = {"Avbryt", "Skapa konto"};
                
                int addAccount = JOptionPane.showOptionDialog(parent, 
                                                              addAccountFormPanel, 
                                                              "Lägg till konto", 
                                                              0, 
                                                              JOptionPane.PLAIN_MESSAGE, 
                                                              null, 
                                                              optionsAddAccountForm, 
                                                              null);
                if (addAccount == 1)
                {
                    if (accountTypeRButtons[0].isSelected())
                        bankLogic.createSavingsAccount(customerPersNo);
                    else
                        bankLogic.createCreditAccount(customerPersNo);
                    ArrayList<String> accounts = bankLogic.getAccountsShortInfo(customerPersNo);
                    updateAccountList(accounts);
                }
            
                    
            }
            
            // Close account-button
            else if (buttonName.equals(addCloseButtonNames[1]) && !accountList.isSelectionEmpty())
            {
                // Confirm dialouge window:
                String confirmDeleteAccountMsg = "Är du säker på att du vill ta bort valt konto?";
                String[] optionsConfirmDeleteAccount = {"Nej", "Ja"};
                int confirmAccountDelete = JOptionPane.showOptionDialog(parent, 
                                             confirmDeleteAccountMsg, 
                                             "Ta bort konto", 
                                             0, 
                                             JOptionPane.WARNING_MESSAGE, 
                                             null, 
                                             optionsConfirmDeleteAccount, 
                                             0);
                
                if (confirmAccountDelete == 1)
                {
                    // deletion of the account in the underlying bankLogic system:
                    String deletedAccountMessage = bankLogic.closeAccount(customerPersNo, customerAccountId);
                    
                    // The deleted account-info is displayed in a message dialog
                    JPanel deletionPanel = new JPanel(new BorderLayout());
                    JLabel deletionInfoLabel = new JLabel("Information om borttaget konto:");
                    JTextArea deletionText = new JTextArea(deletedAccountMessage);
                    deletionText.setEditable(false);
                    JLabel deletionInfoLabel2 = new JLabel("(Konto) (Saldo) (Kontotyp) (Ränta)");
                    deletionPanel.add(deletionInfoLabel, BorderLayout.NORTH);
                    deletionPanel.add(deletionText, BorderLayout.CENTER);
                    deletionPanel.add(deletionInfoLabel2, BorderLayout.SOUTH);
                    JOptionPane.showMessageDialog(parent, deletionPanel, "Valt konto borttaget", JOptionPane.INFORMATION_MESSAGE);
                    
                    // The graphical accountList is updated:
                    ArrayList<String> accounts = bankLogic.getAccountsShortInfo(customerPersNo);
                    updateAccountList(accounts);
                }
            }
        }
        
    }

    
    /**
     * Creates the list where all the accounts belonging
     * to a customer can be seen.
     */
    private void createAccountList()
    {
        accountListItems = new DefaultListModel<String>();
        accountList = new JList<String>();
        accountList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        accountList.addListSelectionListener(new AccountListListener());
        JScrollPane accountScrollPane = new JScrollPane(accountList);
        accountScrollPane.setPreferredSize(new Dimension(400, 100));
        accountPanel.add(accountScrollPane);
        
    }
    /**
     * Listens to selections in the account list
     * and updates the Account Information labels
     * according to the selected account.
     * 
     * @author Loe Lindström, loelin-8
     */
    class AccountListListener implements ListSelectionListener
    {
        @Override
        public void valueChanged(ListSelectionEvent e)
        {   
            if (e.getValueIsAdjusting() == false && !accountList.isSelectionEmpty()) {
                updateAccountInfo();
            }
        }
        
    }

    
    /**
     * Creates the labels where the
     * info about a selected account
     * is shown.
     */
    private void createAccountInfo()
    {
        Dimension dimension = new Dimension(190, 60);
        
        accountInfoLeft = new JTextArea("");
        accountInfoLeft.setEditable(false);
        accountInfoLeft.setBackground(this.getBackground());
        accountInfoLeft.setPreferredSize(dimension);
        
        accountInfoRight = new JTextArea("");
        accountInfoRight.setEditable(false);
        accountInfoRight.setBackground(this.getBackground());
        accountInfoRight.setPreferredSize(dimension);
        
        accountPanel.add(accountInfoLeft);
        accountPanel.add(accountInfoRight);
    }

    
    /**
     * Creates the buttons for actions related
     * to a account which is selected in the "accountList"
     * such as withdrawing and depositing money
     * or view the transaction history of the
     * account. 
     */
    private void createAccountActionButtons()
    {
        accountActionButtons = new JButton[accountActionButtonNames.length];
        
        ActionListener accountActionListener = new AccountActionButtonsListener();
        for (int i = 0; i < accountActionButtonNames.length; i++)
        {
            accountActionButtons[i] = new JButton(accountActionButtonNames[i]);
            accountActionButtons[i].addActionListener(accountActionListener);
            accountPanel.add(accountActionButtons[i]);
        }
        
    }
    /**
     * Inner class listening to the buttons
     * for depositing, withdrawal and view transactions.
     * @author Loe Lindström, loelin-8
     *
     */
    class AccountActionButtonsListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e)
        {
            String buttonName = ((JButton)e.getSource()).getText();
            
            // Deposit-button:
            if (buttonName.equals(accountActionButtonNames[0]) && !accountList.isSelectionEmpty()) 
            {
                JPanel depositPanel = new JPanel();
                JLabel depositInfo = new JLabel("Hur mycket pengar vill du sätta in?");
                JTextField depositAmount = new JTextField(10);
                JLabel depositCurrency = new JLabel("sek");
                depositPanel.add(depositInfo);
                depositPanel.add(depositAmount);
                depositPanel.add(depositCurrency);
                
                String[] optionsDeposit = {"Avbryt", "Sätt in"};
                int confirmDeposit = JOptionPane.showOptionDialog(parent, 
                                                                  depositPanel, 
                                                                  "Insättning", 
                                                                  0, 
                                                                  JOptionPane.PLAIN_MESSAGE, 
                                                                  null, 
                                                                  optionsDeposit, 
                                                                  null);
            
                // If user confirms deposit the deposit is made:
                if (confirmDeposit == 1)
                {
                    try 
                    {
                        double amount = Double.parseDouble(depositAmount.getText());
                        bankLogic.deposit(customerPersNo, customerAccountId, amount);
                        updateAccountList(bankLogic.getAccountsShortInfo(customerPersNo));
                        updateAccountInfo();
                    }
                    // Show error message with info if the user's amount is invalid:
                    catch (NumberFormatException Exception) 
                    {
                        JOptionPane.showMessageDialog(parent, "Insättningen misslyckades.\nAnge belopp i siffror och vid decimalbelopp använd punkt", "Misslyckades", JOptionPane.ERROR_MESSAGE);
                    }
                    
                }
                    
            }
            
            // Withdrawal:
            if (buttonName.equals(accountActionButtonNames[1]) && !accountList.isSelectionEmpty())
            {
                JPanel withdrawalPanel = new JPanel();
                JLabel withdrawalInfo = new JLabel("Hur mycket pengar vill du ta ut?");
                JTextField withdrawalAmount = new JTextField(10);
                JLabel withdrawalCurrency = new JLabel("sek");
                withdrawalPanel.add(withdrawalInfo);
                withdrawalPanel.add(withdrawalAmount);
                withdrawalPanel.add(withdrawalCurrency);
                
                String[] optionsWithdrawal = {"Avbryt", "Ta ut"};
                int confirmWithdrawal = JOptionPane.showOptionDialog(parent, 
                                                                  withdrawalPanel, 
                                                                  "Uttag", 
                                                                  0, 
                                                                  JOptionPane.PLAIN_MESSAGE, 
                                                                  null, 
                                                                  optionsWithdrawal, 
                                                                  null);
                // If users confirm the withdrawal is made if 
                // the user-specified amount is valid.
                if (confirmWithdrawal == 1)
                {   
                    try 
                    {
                        double amount = Double.parseDouble(withdrawalAmount.getText());
                        boolean success = bankLogic.withdraw(customerPersNo, customerAccountId, amount);
                        // Show error message with info if saldo was too low:
                        if (!success)
                        {
                            JOptionPane.showMessageDialog(parent, "Uttaget misslyckades för att saldot var för lågt", "Misslyckades", JOptionPane.ERROR_MESSAGE);
                        }
                        updateAccountList(bankLogic.getAccountsShortInfo(customerPersNo));
                        updateAccountInfo();
                    }
                    // Show error message with info if the user's amount is invalid:
                    catch (NumberFormatException Exception) 
                    {
                        JOptionPane.showMessageDialog(parent, "Uttaget misslyckades.\nAnge belopp i siffror och vid decimalbelopp använd punkt", "Misslyckades", JOptionPane.ERROR_MESSAGE);
                    }
                    
                }
                    
            }
            
            // See transactions:
            if (buttonName.equals(accountActionButtonNames[2]) && !accountList.isSelectionEmpty())
            {
                JPanel transactionsPanel = new JPanel();
                ArrayList<String> transactions = bankLogic.getTransactions(customerPersNo, customerAccountId);
                DefaultListModel<String> transactionsListItems = new DefaultListModel<String>();
                
                if (transactions.isEmpty())
                    transactionsListItems.addElement("Inga transaktioner");
                else
                    transactionsListItems.addAll(transactions);
                
                JList<String> transactionsList = new JList<String>(transactionsListItems);
                transactionsPanel.add(transactionsList);
                
                String[] optionsTransactions = {"Stäng", "Exportera"};
                
                int responseTransactions = JOptionPane.showOptionDialog(parent, 
                                                                        transactionsPanel, 
                                                                        "Transaktioner", 
                                                                        0, 
                                                                        JOptionPane.PLAIN_MESSAGE, 
                                                                        null, 
                                                                        optionsTransactions, 
                                                                        null);
                 
                // Export (Gets added in a later version)
                if (responseTransactions == 1)
                {
                    
                }
            }
        }
    }
    
    /**
     * Update the Info label with the customer info
     * of the selected customer in the JPanel
     * "customerListPanel". 
     * (This function is called from the
     * parent window "BankGUI".)
     */
    public void updateCustomerInfoLabel(String name, String persNo)
    {
        customerPersNo = persNo;
        if (name.isEmpty())
            customerInfo.setText("");
        else
            customerInfo.setText(String.format("Namn: %s%nPersnr: %s", name, persNo));
    }
    
    /**
     * Makes the graphical account-list empty. 
     */
    public void clearAccountList()
    {
        accountListItems.clear();
        accountList.setModel(accountListItems);
        accountInfoLeft.setText("");
        accountInfoRight.setText("");
    }
    
    
    /**
     * Updates the account list based on which customer is selected 
     * in the JPanel CustomerListPanel. (This method is called
     * through the parent BankGUI.)
     * 
     * @param accounts ArrayList<String> with all the accounts.
     */
    public void updateAccountList(ArrayList<String> accounts)
    {
        accountListItems.clear();
        accountListItems.addAll(accounts);
        accountList.setModel(accountListItems);
        accountList.setSelectedIndex(0);
        updateAccountInfo();

    }
    
    /**
     * Updates the private field customerAccountId to
     * be concurrent with the account which is selected in the "accountList".
     */
    private void updateCustomerAccountId()
    {
        String selectedAccount = accountList.getSelectedValue();
        int end = selectedAccount.indexOf(" ");
        customerAccountId = Integer.parseInt(selectedAccount.substring(0, end));
    }
    
    /**
     * Updates the JTextAreas displaying more detailed information about
     * the account which is selected in the accountList.
     */
    private void updateAccountInfo()
    {
        if (!bankLogic.getAccountsShortInfo(customerPersNo).isEmpty())
        {
            updateCustomerAccountId();
        
            ArrayList<String> accountInfoLong = bankLogic.getAccountInfoLong(customerPersNo, customerAccountId);
            if (accountInfoLong != null)
            {
                accountInfoLeft.setText(accountInfoLong.get(0));
                accountInfoRight.setText(accountInfoLong.get(1));
            }
        }
        else
        {
            accountInfoLeft.setText("");
            accountInfoRight.setText("");
        }
        
    }
}
