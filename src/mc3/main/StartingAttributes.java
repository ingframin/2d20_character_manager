package mc3.main;

import javax.swing.*;
import static javax.swing.GroupLayout.Alignment.LEADING;
import static javax.swing.LayoutStyle.ComponentPlacement.RELATED;

public class StartingAttributes extends JPanel {

    public StartingAttributes(){
        super();
        var gl = new GroupLayout(this);
        this.setLayout(gl);
        var lbl = new JLabel("Name:");
        var field = new JTextField(15);
        var button = new JButton("Provola");

        GroupLayout.SequentialGroup sg = gl.createSequentialGroup();

        sg.addComponent(lbl).addPreferredGap(RELATED).addComponent(field,
                GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE,
                GroupLayout.PREFERRED_SIZE).addPreferredGap(RELATED).addComponent(button);

        gl.setHorizontalGroup(sg);

        GroupLayout.ParallelGroup pg = gl.createParallelGroup(
                LEADING, false);

        pg.addComponent(lbl).addComponent(field).addComponent(button);
        
        gl.setVerticalGroup(pg);

        gl.setAutoCreateContainerGaps(true);


    }
    
}
