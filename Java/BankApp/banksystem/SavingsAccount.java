package loelin8.banksystem;

import java.util.ArrayList;

/**
 * SavingsAccount()
 * A concrete Account()-child.
 * To store information about a Savings Account 
 * as well as make deposits/withdrawals from it
 * with the right rates. 
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class SavingsAccount extends Account
{
    private static final double interestRate = 1.0;
    private static final double withdrawRate = 2.0;
    private int withdrawsPerYear;
    private static final String ACCOUNT_TYPE = "Sparkonto";
    
    public SavingsAccount()
    {
        super();
    }
    
    public SavingsAccount(double saldo) throws Exception
    {
       super(saldo);
       if (saldo < 0)
       {
           throw new Exception("You cannot open a SavingsAccount with a negative saldo.");
       }
       
       withdrawsPerYear = 0;
    }
    
    @Override
    public boolean withdraw(double amount)
    {
        if (this.withdrawsPerYear > 0)
        {
            amount += amount * SavingsAccount.getWithdrawRate() / 100;
        }
        
        if (amount > this.getSaldo())
        {
            return false;
        }
        
        else {
            this.setSaldo(this.getSaldo() - amount);
            this.setWithdrawsPerYear(this.withdrawsPerYear + 1);
            return true;
        }
    }
    
    @Override
    public String toString()
    {   
        return String.format("%d %.1f kr Sparkonto %.1f %%", 
                super.getAccountId(), super.getSaldo(), interestRate);
    }
    
    @Override
    public String toStringShort()
    {
        return String.format("%d Sparkonto %.1f sek", 
                super.getAccountId(), super.getSaldo());
    }
    
    @Override
    public String toStringClosedAccount()
    {
        double interestAmount = calculateInterest();
        return String.format("%d %.1f kr %s %.1f kr", super.getAccountId(), 
                super.getSaldo(), ACCOUNT_TYPE, interestAmount);
    }

    @Override
    public ArrayList<String> getAccountInfoLong()
    {
        ArrayList<String> accountInfoLong = new ArrayList<>();
        
        String accountInfoLeft = String.format("Kontonr:  %d%n"
                + "Kontotyp: %s%n"
                + "Saldo:      %.2f", 
         this.getAccountId(), ACCOUNT_TYPE, this.getSaldo());
        
        String accountInfoRight = String.format("Räntesats:   %.2f %%%n"
                + "Antal Uttag: %d%n",
                this.interestRate, this.withdrawsPerYear);
        
        accountInfoLong.add(accountInfoLeft);
        accountInfoLong.add(accountInfoRight);
        return accountInfoLong;
    }
    
    @Override
    public double calculateInterest()
    {
        return this.getSaldo() * SavingsAccount.interestRate / 100;
    }
    
    
    @Override
    public double getSaldo()
    {
        return super.getSaldo();
    }

    @Override
    public void setSaldo(double saldo)
    {
        super.setSaldo(saldo);
    }

    @Override
    public int getAccountId()
    {
        return super.getAccountId();
    }

    public int getWithdrawsPerYear()
    {
        return withdrawsPerYear;
    }

    public void setWithdrawsPerYear(int withdrawsPerYear)
    {
        this.withdrawsPerYear = withdrawsPerYear;
    }

    public static double getWithdrawRate()
    {
        return withdrawRate;
    }


    
    
}
