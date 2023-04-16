package mc3.gui;

import javax.swing.*;
import static javax.swing.GroupLayout.Alignment.LEADING;
import static javax.swing.LayoutStyle.ComponentPlacement.RELATED;

import java.awt.*;
import javax.swing.*;

public class StartingAttributes extends JPanel {
  /**
	 * 
	 */
	private static final long serialVersionUID = -9015182584141474439L;

// An array of labels for the text fields
  private static final String[] LABELS = {
    "Agility", "Awareness", "Coordination", "Intelligence",
    "Mental", "Personality", "Physique", "Strength"
  };

  // An array of text fields
  private final JTextField[] fields = new JTextField[LABELS.length];

  // The "next" button
  private final JButton nextButton = new JButton("Next");

  public StartingAttributes() {
    // Set the layout to a grid layout with 1 column and 9 rows
    setLayout(new GridLayout(9, 1));

    // Add a label and text field for each attribute
    for (int i = 0; i < LABELS.length; i++) {
      // Create the label and text field
      JLabel label = new JLabel(LABELS[i]);
      fields[i] = new JTextField("5", 2); // Initialise the text field to 5

      // Create the "increase" and "decrease" buttons
      JButton increaseButton = new JButton("+");
      JButton decreaseButton = new JButton("-");
      
      final int j =i;
      // Add an action listener to the buttons to increase or decrease the value in the text field
      increaseButton.addActionListener(e -> {
        int value = Integer.parseInt(fields[j].getText());
        fields[j].setText(String.valueOf(value + 1));
        checkTotal(); // Check if the total is now equal to 40
      });
      decreaseButton.addActionListener(e -> {
        int value = Integer.parseInt(fields[j].getText());
        fields[j].setText(String.valueOf(value - 1));
        checkTotal(); // Check if the total is now equal to 40
      });

      // Add the label, text field, and buttons to the panel
      add(label);
      add(fields[i]);
      add(increaseButton);
      add(decreaseButton);
    }

    // Add the "next" button to the panel and disable it initially
    nextButton.setEnabled(false);
    add(nextButton);
  }

  // A method to check if the total of the values in the text fields is equal to 40
  private void checkTotal() {
    int total = 0;
    for (JTextField field : fields) {
      total += Integer.parseInt(field.getText());
    }
    nextButton.setEnabled(total == 40);
  }
}
