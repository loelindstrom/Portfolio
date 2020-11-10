package loelin8.banksystem;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * A class for a bank system.
 * Containing customers which can have acocunts in the bank. 
 * See Customer()- and Account()-classes.
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class BankLogic
{
    private ArrayList<Customer> customerRegister;
    private static String timeFormat = "yyyy-MM-dd HH:mm:ss";
    
    public BankLogic() {
        customerRegister = new ArrayList<Customer>();
    }
    
    /**
     * Gets the personal information of all the customers in the bank
     * in the form of an ArrayList<String> where each element
     * is the information about one customer. 
     * 
     * @return ArrayList<String> with all customers currently in the bank.
     */
    public ArrayList<String> getAllCustomers()
    {
        ArrayList<String> allCustomers = new ArrayList<>();
        for (Customer customer : customerRegister)
        {
            String customerString = String.format("%s %s %s", 
                    customer.getpNo(), customer.getName(), customer.getSurname());
            allCustomers.add(customerString);
        }
        
        return allCustomers;
    }
    
    /**
     * Adds a customer to the bank.
     * But only if it doesn't already
     * exist a customer with the personal number specified.
     * 
     * @param name = First name of the customer
     * @param surname = Last name of the customer
     * @param pNo = Personal number of the customer
     * 
     * @return True if new customer was created. 
     *         False if a customer with that personal number already exists in the bank. 
     */
    public boolean createCustomer(String name, String surname, String pNo)
    {
        if (indexOfCustomer(pNo) >= 0)
        {
            return false;
        }
        
        else
        {
            Customer customer = new Customer(name, surname, pNo);
            customerRegister.add(customer);
            return true;
        }
    }
    
    /**
     * Gets information about a customer in the form
     * of an ArrayList<String> where the first
     * element is personal information of the customer (Pers. no, name, surname)
     * and the other elements are each account connected to the customer 
     * with corresponding account-information. 
     * 
     * @param pNo = Customer's personal number
     * 
     * @return ArrayList<String> or Null if customer doesn't exist.
     */
    public ArrayList<String> getCustomer(String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {    
            return customer.getCustomerInfo();
        }
        
        else
            return null;
    }
    
    /**
     * Changes the name of a customer with the given personal number.
     * 
     * @param name = Customer's new first name
     * @param surname = Customer's new last name
     * @param pNo = Customer's personal number
     * @return true if name change was done. Otherwise false. 
     */
    public boolean changeCustomerName(String name, String surname, String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {            
            boolean success = false;
            if (!name.isEmpty())
            {
                customer.setName(name);
                success = true;
            }
            
            if (!surname.isEmpty())
            {
                customer.setSurname(surname);
                success = true;
            }
            
            return success;
        }
        
        return false;
    }
    
    /**
     * Adds a new account to a customer.
     * The customer is specified with the customer's personal number.
     * 
     * @param pNo = Existing customers personal number
     * 
     * @return = The account-ID of the created account.
     *           If customer doesn't exist -1 is returned.
     */
    public int createSavingsAccount(String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            int addedAccountNo = customer.addSavingsAccount();
            return addedAccountNo;
        }
        
        return -1;
    }
    
    /**
     * Adds a new credit account to a customer.
     * The customer is specified with the customer's personal number.
     * 
     * @param pNo = Existing customers personal number
     * 
     * @return = The account-ID of the created account.
     *           If customer doesn't exist -1 is returned.
     */
    public int createCreditAccount(String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            int addedAccountNo = customer.addCreditAccount();
            return addedAccountNo;
        }
        
        return -1;
    }
    
    /**
     * Gets info about a customer's account.
     * To get the info the customer's name and account-ID
     * must be specified. 
     * 
     * @param pNo = customer's personal number
     * @param accountId = customer's account-ID
     * @return A String with the folowing info: 
     *              - Account-ID
     *              - Saldo
     *              - Type of account
     *              - Interest rate
     *              
     *         Null if no account was found.
     */
    public String getAccount(String pNo, int accountId)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            Account account = customer.getAccount(accountId);
            if (account != null)
            {
                return account.toString();
            }
        }
        
        return null;
    }
    
    /**
     * Gets information about the accounts of a
     * customer (through customer's personal number)
     * and returns it in the form of an ArrayList<>.
     * 
     * Each element in the array contains a String with 
     * the following info:
     *   - account no.
     *   - account type
     *   - saldo
     * @param pNo int personal number
     * @return ArrayList<String>
     */
    public ArrayList<String> getAccountsShortInfo(String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            return customer.getAccountsShortInfo();
        }
        return null;
    }
    
    public ArrayList<String> getAccountInfoLong(String pNo, int accountId)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            Account account = customer.getAccount(accountId);
            if (account != null)
            {
                return account.getAccountInfoLong();
            }
        }
        return null;
    }
    
    /**
     * Returns all transactions for a customer's account.
     * Customer specified by pNo.
     * Account specified by accountId
     * 
     * @param pNo String
     * @param accountId int
     * @return ArrayList<String> with transactions
     */
    public ArrayList<String> getTransactions(String pNo, int accountId)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            Account account = customer.getAccount(accountId);
            if (account != null)
            {
                return account.getTransactions();
            }
        }
        return null;
    }
    
    /**
     * Makes a deposit to a customer's specific account.
     * Only makes a deposit if the specified amount
     * is bigger than zero.
     * 
     * @param pNo = String customer's personal number
     * @param accountId = int account number
     * @param amount = double amount to deposit 
     * 
     * @return true if deposit was made. Otherwise false.
     */
    public boolean deposit(String pNo, int accountId, double amount)
    {
        if (amount <= 0)
        {
            return false;
        }
        
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            Account account = customer.getAccount(accountId);
            if (account != null)
            {   
                account.setSaldo(account.getSaldo() + amount);
                recordTransaction(account, amount);
                
                return true;
            }
        }
        
        return false;
    }
    
    /**
     * Withdraws money from a given customer's given account.
     * But only if the amount specified is available on the account
     * and the amount is larger than zero.
     * 
     * @param pNo = String customer's personal number
     * @param accountId = int customer's account-ID
     * @param amount = double amount to be withdrawn
     * 
     * @return true if withdrawn was made. false otherwise.
     */
    public boolean withdraw(String pNo, int accountId, double amount)
    {
        if (amount <= 0)
            return false;
        
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            Account account = customer.getAccount(accountId);
            if (account != null)
            {
                if (account.withdraw(amount))
                {
                    recordTransaction(account, -amount);
                    return true;
                }
                else
                {
                    return false;
                }
                                    
            }
        }
        
        return false;
    }
    
    /**
     * Closes a customer's account and removes it from the bank.
     * Returns information about the account
     * with the actual interest amount based on one year's
     * interest rate insted of the interest rate.
     * 
     * @param pNo = customer's personal number
     * @param accountId = customer's account-ID
     * 
     * @return A String with the folowing info: 
     *              - Account-ID
     *              - Saldo
     *              - Type of account
     *              - Interest amount
     *         Returns null if no account was closed.
     */
    public String closeAccount(String pNo, int accountId)
    {
        Customer customer = findCustomer(pNo);
        
        if (customer != null)
        {
            return customer.removeAccount(accountId);
        }
        
        return null;
    }
    
    /**
     * Deletes a customer and all his/her
     * corresponding accounts.
     * Returns back information about the customer
     * and each account that was closed.
     * 
     * @param pNo
     * @return
     */
    public ArrayList<String> deleteCustomer(String pNo)
    {
        Customer customer = findCustomer(pNo);
        if (customer != null)
        {
            ArrayList<String> deletedCustomerInfo = customer.deleteAllAccounts();
            customerRegister.remove(customer);
            return deletedCustomerInfo;
        }
        
        return null;
    }
    
    /**
     * Help function to iterate through the customers
     * of the bank to see if a customer with a certain
     * personal number exists.
     * 
     * @param pNo = Customer's personal number.
     * @return int Index of where in the customerRegister the customer exists.
     *         -1 if customer doesn't exist.
     */
    private int indexOfCustomer(String pNo)
    {   
        int index = 0;
        for (Customer customer : customerRegister)
        {
            if (customer.getpNo().equals(pNo))
            {
                return index;
            }
            index++;
        }
        
        return -1;
    }
    
    /**
     * Help function that returns an existing customer
     * based on the customer's personal number.
     * If no customer w. the pers. no exist null is returned.
     * 
     * @param pNo = customer's personal number
     * 
     * @return Customer() or Null
     */
    private Customer findCustomer(String pNo)
    {   
        int customerIndex = indexOfCustomer(pNo);
        if (customerIndex >= 0)
        {   
            return customerRegister.get(customerIndex);
        }
        
        return null;
    }
    
    /**
     * Adds to an Account()'s transactions history what time and date,
     * how much was deposited/withdrawn 
     * and the remaining saldo
     * 
     * @param account Account()-object
     * @param amount double positive = deposit, negative = withdrawal
     */
    private void recordTransaction(Account account, double amount)
    {
        SimpleDateFormat sdf = new SimpleDateFormat(timeFormat);
        String dateString = sdf.format(new Date());
        String transInfo = dateString + String.format(" %.1f kr Saldo: %.1f kr", 
                amount, account.getSaldo());
        account.addTransactionInfo(transInfo);
    }
}
