package loelin8.gui;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;
import javax.swing.border.TitledBorder;

import loelin8.banksystem.BankLogic;

/**
 * A JPanel inheriting class which is used by its
 * "parent" - a BankGUI instance to add customers to 
 * a banksystem ("bankLogic").
 * 
 * This JPanel contains two panels with different functionalities: 
 *  One for adding customers manually.
 *  One for importing customers from a file.
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class AddCustomerPanel extends JPanel
{   
    // Parent window:
    private BankGUI parent;
    
    // The underlying system-logic of the GUI.
    private BankLogic bankLogic;
    
    private Dimension dimension = new Dimension(420, 150);
    
    // Components for adding a customer to the system manually:
    private JPanel addManuallyPanel;
    private String[] labelNames = {"Förnamn:", "Efternamn:", "Personnr (ÅÅMMDDXXX):"};
    private JLabel[] labels;
    private JTextField[] textFields;
    private JButton addButton;
    
    // Component holding error and success messages:
    private JTextArea errorSuccessLabel;
    
    // Components for adding customers by importing from a file:
    private JPanel importPanel;
    private JLabel filepathLabel;
    private JTextField filepathField;
    private JButton browseButton;
    private JButton importButton;
    
    public AddCustomerPanel(BankGUI parent, BankLogic bankLogic)
    {
        this.parent = parent;
        
        this.bankLogic = bankLogic;
        
        this.setLayout(new GridLayout(4,1));
        
        createAddManuallyPanel();
        createErrorSuccessLabel();
        createImportPanel();
    }
    
    /**
     * Creates the GUI-panel that holds fields for adding a customer
     * manually to the system.
     */
    private void createAddManuallyPanel()
    {   
        
        // The title-framed panel containing the labels, textfields
        // and the add-button.
        addManuallyPanel = new JPanel();
        addManuallyPanel.setLayout(new GridLayout(4, 2));
        TitledBorder title = BorderFactory.createTitledBorder("Lägg till manuellt");
        addManuallyPanel.setBorder(title);
        addManuallyPanel.setPreferredSize(dimension);

        // Creation of the labels and textfields:
        labels = new JLabel[labelNames.length];
        textFields = new JTextField[labelNames.length];
        for (int i = 0; i < labelNames.length; i++)
        {
            labels[i] = new JLabel(labelNames[i]);
            textFields[i] = new JTextField(15); 
        }
        
        // Adding the components in an visually
        // good order based on the GridLayout 
        // of the "addManuallyPanel".
        addManuallyPanel.add(labels[0]);        //Fname label
        addManuallyPanel.add(labels[1]);        //Surname label
        addManuallyPanel.add(textFields[0]);    //Fname field
        addManuallyPanel.add(textFields[1]);    //Surname field
        addManuallyPanel.add(labels[2]);        //PersNo label
        addManuallyPanel.add(new JLabel(""));   //Spacing
        addManuallyPanel.add(textFields[2]);    //PersNo field
        addButton = new JButton("Lägg till");
        addButton.addActionListener(new AddManuallyListener());
        addManuallyPanel.add(addButton);
        
        this.add(addManuallyPanel);
    }
    /**
     * Listens to the addButton (when a customer is added manually) and handles
     * errors in the input.
     * @author Loe Lindström, loelin-8
     *
     */
    class AddManuallyListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e)
        {
            String fname = textFields[0].getText();
            String surname = textFields[1].getText();
            String persNo = textFields[2].getText();
            
            // Checks for errors in the input:
            String checkMessage = BankGUI.checkInput(fname, surname, persNo);
            if (!checkMessage.isEmpty())
            {
                errorSuccessLabel.setForeground(Color.red);
                errorSuccessLabel.setText(checkMessage);
            }
            else
            {
                errorSuccessLabel.setForeground(Color.black);
                bankLogic.createCustomer(fname, surname, persNo);
                textFields[0].setText("");
                textFields[1].setText("");
                textFields[2].setText("");
                parent.updateCustomerList();
                String succesMessage = String.format("%s %s med persnr %s är tillagd.", fname, surname, persNo);
                errorSuccessLabel.setText(succesMessage);
            }
          
        }
        
        
        
    }
    
    /**
     * Creates the JTextArea where error or
     * sucess messages are displayed.
     */
    private void createErrorSuccessLabel()
    {
        errorSuccessLabel = new JTextArea("");
        errorSuccessLabel.setBackground(this.getBackground());
        errorSuccessLabel.setEditable(false);
        this.add(errorSuccessLabel);
    }
    
    /**
     * Creates the GUI-panel where one can add a customer
     * from a file to the system.
     */
    private void createImportPanel()
    {
        // The title-framed panel where the user can import customers 
        // to the bank from a file:
        importPanel = new JPanel();
        importPanel.setLayout(new GridLayout(2, 3));
        TitledBorder title = BorderFactory.createTitledBorder("Importera från fil");
        importPanel.setBorder(title);
        importPanel.setPreferredSize(dimension);
        
        // Upper half of the import panel:
        JPanel importPanelUpper = new JPanel();
        importPanelUpper.setLayout(new BorderLayout());
        filepathLabel = new JLabel("Välj fil..");
        filepathField = new JTextField("", 20);
        browseButton = new JButton("Bläddra");
        importPanelUpper.add(new JLabel("  "), BorderLayout.NORTH); //Spacing
        importPanelUpper.add(new JLabel("  "), BorderLayout.SOUTH); //Spacing
        importPanelUpper.add(filepathLabel, BorderLayout.WEST);
        importPanelUpper.add(filepathField, BorderLayout.CENTER);
        importPanelUpper.add(browseButton, BorderLayout.EAST);
        importPanel.add(importPanelUpper);
        
        // Lower half of the import panel:
        JPanel importPanelLower = new JPanel();
        importPanelLower.setLayout(new BorderLayout());
        importButton = new JButton ("Importera");
        importPanelLower.add(new JLabel("  "), BorderLayout.NORTH); //Spacing
        importPanelLower.add(new JLabel("  "), BorderLayout.SOUTH); //Spacing
        importPanelLower.add(importButton);
        importPanel.add(importPanelLower);
        
        this.add(importPanel);
        
    }
}
