package loelin8.gui;

import java.awt.Dimension;
import java.awt.GridLayout;

import javax.swing.*;
import javax.swing.border.TitledBorder;

import loelin8.banksystem.BankLogic;

/**
 * A JPanel which contains a graphical interface
 * to export customer-info in a bank system ("bankLogic") to an external file.
 * This panel is used by its "parent" - a BankGUI-instance.
 * 
 * @author Loe Lindström, loelin-8
 *
 */
public class ExportCustomerPanel extends JPanel
{
    // Parent window:
    private BankGUI parent;
    
    // The underlying system-logic of the GUI.
    private BankLogic bankLogic;
    
    
    // Info about the functionality of the functions in this panel
    private JLabel infoLabel;
    
    // Components for exporting customer-info to an already existing file:
    private JPanel existingFilePanel;
    private JLabel filepathLabelExisting;
    private JTextField filepathFieldExisting;
    private JButton browseButton;
    private JButton exportButton;
    
    // Components for exporting customer-info to a new file:
    private JPanel newFilePanel;
    private JLabel filenameLabelNew;
    private JTextField filenameFieldNew;
    private JButton createButton;
    
    /**
     * A titled-framed JPanel which contains a graphical interface
     * to export customer-info in a bank system to an external file.
     * @param bankLogic an instance of the underlying bank system.
     */
    public ExportCustomerPanel(BankGUI parent, BankLogic bankLogic)
    {
        this.parent = parent;
        
        this.bankLogic = bankLogic;
        
        TitledBorder title = BorderFactory.createTitledBorder("Exportera");
        this.setBorder(title);
        
        infoLabel = new JLabel("Exportera valda kunder till en fil:");
        this.add(infoLabel);
        
        createExistingFilePanel();
        createNewFilePanel();
    }
    
    /**
     * Creating an inner JPanel where
     * the user can export customer info
     * to an already existing file.
     */
    private void createExistingFilePanel()
    {
        // The titled panel:
        existingFilePanel = new JPanel(new GridLayout(2, 3));
        TitledBorder title = BorderFactory.createTitledBorder("Befintlig fil"); 
        existingFilePanel.setBorder(title);
        existingFilePanel.setPreferredSize(new Dimension(400, 100));     
        
        // The components of the inner panel:
        filepathLabelExisting = new JLabel("Välj befintlig fil..");
        filepathFieldExisting = new JTextField(20);
        browseButton = new JButton("Bläddra");
        exportButton = new JButton("Exportera");
        
        // Adding the components and the panel:
        existingFilePanel.add(filepathLabelExisting);
        existingFilePanel.add(filepathFieldExisting);
        existingFilePanel.add(browseButton);
        for (int i = 0; i < 2; i++)
            existingFilePanel.add(new JLabel(""));
        existingFilePanel.add(exportButton);
        this.add(existingFilePanel);
    }
    
    /**
     * Creating an inner JPanel where
     * the user can export customer info
     * to a new file.
     */
    private void createNewFilePanel()
    {
        // The titled panel:
        newFilePanel = new JPanel();
        TitledBorder title = BorderFactory.createTitledBorder("Skapa ny fil"); 
        newFilePanel.setBorder(title);
        newFilePanel.setPreferredSize(new Dimension(400, 100));
        
        // The components of the inner panel:
        filenameLabelNew = new JLabel("Skapa en ny fil:");
        filenameFieldNew = new JTextField("namn.csv", 10);
        createButton = new JButton("Skapa och exportera");
        
        // Adding the components and the panel:
        newFilePanel.add(filenameLabelNew);
        newFilePanel.add(filenameFieldNew);
        newFilePanel.add(createButton);
        this.add(newFilePanel);
    }
}
