package loelin8.banksystem;

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * A class for customers belonging to a bank.
 * And who can have accounts. 
 * See BankLogic()- and Account()-class.
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class Customer
{
    private String name;
    private String surname;
    private final String pNo;
    private ArrayList<Account> customersAccounts = new ArrayList<>();
    
    /**
     * Constructor
     * @param name = Customer's first name
     * @param surname = Customer's last name
     * @param pNo = Customer's personal number
     */
    public Customer(String name, String surname, String pNo)
    {   
        this.name = name;
        this.surname = surname;
        this.pNo = pNo;
    }
    
    /**
     * Creates a bank account (of the class "SavingsAccount()")
     * and attaches is to the customer.
     * 
     * @return The account-ID of the created account
     */
    public int addSavingsAccount() {
        SavingsAccount account = new SavingsAccount();
        customersAccounts.add(account);
        return account.getAccountId();
    }
    
    /**
     * Creates a bank account (of the class "CreditAccount()")
     * and attaches is to the customer.
     * 
     * @return The account-ID of the created account
     */
    public int addCreditAccount() {
        CreditAccount account = new CreditAccount();
        customersAccounts.add(account);
        return account.getAccountId();
    }
    
    /**
     * Removes an account (found by its accountId)
     * and returns a String containing information about
     * the closed account. 
     * @param accountId int
     * @return String closedAccountInfo
     */
    public String removeAccount(int accountId)
    {
        Account account = this.getAccount(accountId);
        if (account != null)
        {
            String closedAccountInfo = account.toStringClosedAccount();
            customersAccounts.remove(account);
            return closedAccountInfo;
        }
        return null;
        
    }
    
    

    /**
     * Checks if a certain account-ID belongs
     * to this customer.
     * If it does the account is returned.
     * Otherwise null is returned.
     * 
     * @param accountId = int Account-ID
     * @return Customer()-object or null
     */
    public Account getAccount(int accountId)
    {
        for (Account account : this.customersAccounts)
        {
            if (accountId == account.getAccountId())
            {
                return account;
            }
        }
        return null;
    }
    
    /**
     * Returns an ArrayList<String> with the customer's
     * name, personal number and information about her accounts.
     * @return ArrayList<String> customerInfo;
     */
    public ArrayList<String> getCustomerInfo()
    {
        if (!customersAccounts.isEmpty())
        {
            ArrayList<String> customerInfo = new ArrayList<>();
            customerInfo.add(this.toString());
            
            for (Account account : customersAccounts)
            {   
                customerInfo.add(account.toString());
            }
    
            return customerInfo;
        }
        return null;
    }
    
    /**
     * Returns an ArrayList with the info about
     * the the customer's accounts.
     * Each element is a String with:
     *   - account no.
     *   - account type
     *   - saldo
     * @return ArrayList<String> accounts
     */
    public ArrayList<String> getAccountsShortInfo()
    {
        ArrayList<String> accounts = new ArrayList<>();
        for (Account account : customersAccounts)
        {
            accounts.add(account.toStringShort());
        }
            
        return accounts;
    }
    
    /**
     * Deletes a customer's accounts and returns an
     * ArrayList<String> where first element
     * is customers name. The rest of the elements
     * are each account that belonged to the customer
     * and close-information about that account (interest rate).
     * 
     * @return ArrayList<String> deletedCustomerInfo
     */
    public ArrayList<String> deleteAllAccounts()
    {
        ArrayList<String> deletedCustomerInfo = new ArrayList<String>();
        deletedCustomerInfo.add(this.toString());
        
        while (!this.customersAccounts.isEmpty())
        {   
            Account account = customersAccounts.get(0);
            String accountInfo = removeAccount(account.getAccountId());
            deletedCustomerInfo.add(accountInfo);
        }
        return deletedCustomerInfo;
    }
    
    @Override
    public String toString()
    {
        return String.format("%s %s %s", pNo, name, surname);
    }    
    
    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }
    
    public String getSurname()
    {
        return surname;
    }
    
    public void setSurname(String surname)
    {
        this.surname = surname;
    }
    
    public String getpNo()
    {
        return pNo;
    }
}
