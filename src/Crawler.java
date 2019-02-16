/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.SocketTimeoutException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.json.JSONException;
import org.json.JSONObject;
import org.jsoup.HttpStatusException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

/**
 *
 * @author Ahmed
 */
public class Crawler {

    public static void main(String args[]) throws JSONException, IOException {
        Document search_result;
        String requested[] = new String[]{"aspirin", "Fentanyl"};
        ArrayList<Newsfeed_item> threads = new ArrayList();
        String query = "https://www.medhelp.org/search/expanded?cat=posts&page=";
        //https://www.medhelp.org/search/expanded?cat=posts&page=1&query=Fentanyl
        try {
            for (int i = 0; i < requested.length; i++) {
                int count = 0;
                for (int j = 1;j<3; j++) {
                    String url = query+ "" + j + "&query=" + requested[i];
                    search_result = Jsoup.connect(url).get();
                    Elements posts = search_result.getElementsByClass("result");
                    for (Element item : posts) {
                        
                        Elements user = item.getElementsByClass("title");
                        Elements link = user.get(0).getElementsByTag("a");
                        Newsfeed_item currentItem = new Newsfeed_item();
                        currentItem.replysLink = link.attr("abs:href");
                        int tries = 0;
                        while (true) {
                            try {
                                Document reply_result = Jsoup.connect(currentItem.replysLink).get();
                                Element description = reply_result.getElementById("subject_msg");
                                Elements userInfo=reply_result.getElementsByClass("subj_info");
                                Element userLink = userInfo.get(0).getElementsByClass("username").get(0).getElementsByTag("a").get(0);
                                
                                Document userInfo_result = Jsoup.connect(userLink.attr("abs:href")).get();
                                Element aboutMe=userInfo_result.getElementsByClass("section").get(0);
                                String[] info;
                                info = aboutMe.text().split("[:\\;\\ \\,]");
                                for (String in:info)
                                {
                                    try{
                                        int number=Integer.parseInt(in);
                                        if(number<1000)
                                        {
                                            currentItem.userAge=String.valueOf(number);
                                        }
                                        else{
                                            currentItem.joiningYear=String.valueOf(number);
                                        }
                                    }
                                    catch (Exception e)
                                    {
                                             if(in.equals("Male") || in.equals("Female"))
                                             {
                                                 currentItem.userGender=in;
                                             }
                                    }
                                }
                                
                                
                                currentItem.description = description.text();
                                currentItem.subject = requested[i];
                                System.out.println((count++) + ":" + currentItem);
                                threads.add(currentItem);
                                break;
                            } catch (HttpStatusException e) {
                                System.out.println("Ignore this post");
                                break;
                            } catch (SocketTimeoutException e2) {
                                System.out.println("Connection Timeout");
                                if (tries++ == 3) {
                                    break;
                                }
                            }
                        }
                    }
                    
                    if (count == 20) {
                        break;
                    }
                }

            }

            System.out.println(threads.size());
            writeToCSV(threads);
        } catch (IOException ex) {
            Logger.getLogger(Crawler.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    public static String jsonGetRequest(String urlQueryString) {
        String json = null;
        try {
            java.net.URL url = new java.net.URL(urlQueryString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setDoOutput(true);
            connection.setInstanceFollowRedirects(false);
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("charset", "utf-8");
            connection.connect();
            InputStream inStream = connection.getInputStream();
            json = streamToString(inStream); // input stream to string
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return json;
    }

    private static final String CSV_SEPARATOR = ",";

    private static void writeToCSV(ArrayList<Newsfeed_item> productList) {
        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("posts.csv"), "UTF-8"));
            StringBuilder oneLine = new StringBuilder();
            oneLine.append("Drug,Content,Joined,Age,Gender");
            bw.write(oneLine.toString());
            bw.newLine();
            for (Newsfeed_item product : productList) {
                oneLine = new StringBuilder();
                oneLine.append(product.subject);
                oneLine.append(CSV_SEPARATOR);
                oneLine.append(product.description.replaceAll(",", ";"));
                oneLine.append(CSV_SEPARATOR);
                oneLine.append(product.joiningYear);
                oneLine.append(CSV_SEPARATOR);
                oneLine.append(product.userAge);
                oneLine.append(CSV_SEPARATOR);
                oneLine.append(product.userGender);
                bw.write(oneLine.toString());
                bw.newLine();
            }
            bw.flush();
            bw.close();
        } catch (UnsupportedEncodingException e) {
        } catch (FileNotFoundException e) {
        } catch (IOException e) {
        }
    }

    private static String streamToString(InputStream inputStream) {
        String text = new Scanner(inputStream, "UTF-8").useDelimiter("\\Z").next();
        return text;
    }
}
