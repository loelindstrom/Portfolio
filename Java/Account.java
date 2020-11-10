package loelin8.banksystem;

import java.util.ArrayList;

/**
 * An abstract class for Accounts in a bank.
 * Different Account-types inherits from this class.
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public abstract class Account
{
    private double saldo;
    private final int accountId;
    private static int lastAccountCreated = 1000;
    private ArrayList<String> transactions = new ArrayList<>();
    
    public Account()
    {
        saldo = 0;
        accountId = lastAccountCreated++ + 1;
    }
    
    public Account(double saldo)
    {
        this.saldo = saldo;
        accountId = lastAccountCreated++ + 1;
    }
    
    /**
     * Makes a withdrawal from the account with the specified amount.
     * Granted that the specified amount is valid.
     * @param amount double - the amount of money to be withdrawn.
     * @return true if withdrawal was made.
     */
    public abstract boolean withdraw(double amount);
    
    
    /**
     * Returns a formated string with info about
     * an Account when it is active.
     * @return String
     */
    public abstract String toString();
    
    /**
     * Returns a formated string with info about
     * an Account when it is active in a shorter form.
     * @return String
     */
    public abstract String toStringShort();
    
    /**
     * Returns a formated string with info about
     * an Account when it is closed.
     * @return String
     */
    public abstract String toStringClosedAccount();
    
    
    /**
     * Returns detailed information about an account
     * divided in two strings placed in the returned
     * ArrayList<String>. 
     * To be used for the BankGUI. The first element is to be placed in the left
     * JTextArea "accountInfoLeft" in the CustomerInfoPanel 
     * and the second element in the right JTextArea "accountInfoRight".
     * @return ArrayList<String>
     */
    public abstract ArrayList<String> getAccountInfoLong();
    
    /**
     * Calculates and returns the interest 
     * of an account's saldo. Used especially when an Account is closed.
     * 
     * @return
     */
    public abstract double calculateInterest();
    
    /**
     * 
     * @return double
     */
    public double getSaldo()
    {
        return saldo;
    }

    /**
     * 
     * @param saldo double
     */
    public void setSaldo(double saldo)
    {
        this.saldo = saldo;
    }
    
    /**
     * 
     * @return int
     */
    public int getAccountId()
    {
        return accountId;
    }

    /**
     * 
     * @return int
     */
    public static int getLastaccountcreated()
    {
        return lastAccountCreated;
    }
    
    /**
     * 
     * @return ArrayList<String>
     */
    public ArrayList<String> getTransactions()
    {
        return transactions;
    }

    /**
     * 
     * @param transInfo String
     */
    public void addTransactionInfo(String transInfo)
    {
        this.transactions.add(transInfo);
    }
    
}
