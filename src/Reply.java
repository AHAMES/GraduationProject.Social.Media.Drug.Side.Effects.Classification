
import java.util.Date;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ahmed
 */
public class Reply {
    String commentText;
    String user;
     @Override
    public String toString()
    {
        String item=user+"\n"+commentText+"\n\n";
        item+="===========================================\n";
        return item;
    }
}
