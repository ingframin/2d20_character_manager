package mc3.main;

import javax.swing.SwingUtilities;

public class CharGen{

    public static void main(String[] args){
        System.out.println("test");
        SwingUtilities.invokeLater(()->{new MainFrame();});

    }
}