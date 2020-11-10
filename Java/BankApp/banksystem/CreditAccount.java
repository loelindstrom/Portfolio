package loelin8.banksystem;

import java.util.ArrayList;

/**
 * CreditAccount()
 * A concrete Account()-child.
 * To store information about a Credit Account 
 * as well as make deposits/withdrawals from it
 * with the right rates. 
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class CreditAccount extends Account
{
    private static final double interestRate = 0.5;
    private static final double debtRate = 7;
    private static final int creditLimit = -5000;
    private static final String ACCOUNT_TYPE = "Kreditkonto";
    
    public CreditAccount()
    {
        super();
    }
    
    public CreditAccount(double saldo) throws Exception
    {
        super(saldo);
        if (saldo < creditLimit)
        {
            throw new Exception("Cannot create a CreditAccount with that low saldo");
        }
    }
    
    @Override
    public boolean withdraw(double amount)
    {
        double newSaldo = getSaldo() - amount;
        
        if (newSaldo < -5000)
            return false;
        else
        {
            setSaldo(newSaldo);
            return true;
        }
    }

    @Override
    public String toString()
    {
        return String.format("%d %.1f kr %s %.1f %% ", 
                super.getAccountId(), super.getSaldo(), ACCOUNT_TYPE, interestRate);
    }
    
    @Override
    public String toStringShort()
    {
        return String.format("%d %s %.1f sek", 
                super.getAccountId(), ACCOUNT_TYPE, super.getSaldo());
    }
    
    public String toStringClosedAccount2()
    {
        if (super.getSaldo() < 0)
        {
            double debtAmount = super.getSaldo() * debtRate / 100;
            return String.format("%d %.1f kr %s %.1f kr", super.getAccountId(), 
                    super.getSaldo(), ACCOUNT_TYPE, debtAmount);
        }
        else
        {
            double interestAmount = super.getSaldo() * interestRate / 100;
            return String.format("%d %.1f kr %s %.1f kr", super.getAccountId(), 
                    super.getSaldo(), ACCOUNT_TYPE, interestAmount);
        }
    }
    
    @Override
    public String toStringClosedAccount()
    {
        double interestOrExtraDebt = calculateInterest();
        
        return String.format("%d %.1f kr %s %.1f kr", super.getAccountId(), 
                super.getSaldo(), ACCOUNT_TYPE, interestOrExtraDebt);
    }
    
    @Override
    public ArrayList<String> getAccountInfoLong()
    {
        ArrayList<String> accountInfoLong = new ArrayList<>();
        
        String accountInfoLeft = String.format("Kontonr:  %d%n"
                + "Kontotyp: %s%n"
                + "Saldo:      %.2f", 
         this.getAccountId(), ACCOUNT_TYPE, this.getSaldo());
        
        String accountInfoRight = String.format("Sparränta:    %.1f %%%n"
                                               + "Skuldränta:  %.1f %%%n"
                                               + "Kreditgräns: %d", 
           interestRate, debtRate, creditLimit);
        
        accountInfoLong.add(accountInfoLeft);
        accountInfoLong.add(accountInfoRight);
        
        return accountInfoLong;
    }

    @Override
    /**
     * Calculates the interest of an account.
     * uses different rates depending on if 
     * the saldo of the account is positive or negative.
     * 
     * @return: double interest (positive) debt (negative)
     */
    public double calculateInterest()
    {   
        double ans;
        if (this.getSaldo() < 0)
        {   
            ans = getSaldo() * debtRate / 100;
            return Math.round(ans*1.0)/1.0;
        }
        ans = getSaldo() * interestRate / 100;
        return Math.round(ans*1.0)/1.0;
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

    public static int getCreditlimit()
    {
        return creditLimit;
    }
    
    
}
