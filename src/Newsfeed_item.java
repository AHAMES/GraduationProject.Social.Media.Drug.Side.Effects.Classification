
import java.util.ArrayList;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Ahmed
 */
public class Newsfeed_item {

    String subject;
    String description;
    String userGender;
    String userAge;
    String joiningYear;
    String yearPosted;
    String replysLink;
    ArrayList<Reply> replies;

    public Newsfeed_item() {
        this.replies = new ArrayList();
        userAge="";
        joiningYear="";
        userGender="";
    }

    @Override
    public String toString() {
        String item = subject + "\n" + description + "\n\n";
        item+="+++++++++++++++++++++++++++++++++++++++++++++++++++\n";
        for (Reply r : replies) {
            item+=r;
        }
        item+="+++++++++++++++++++++++++++++++++++++++++++++++++++\n";
        return item;
    }
}
