import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

/**
 * Created for learning porpouse.
 * @author Bluewolf787
 */

public class HttpServer
{

    public static void main(String[] args) throws Exception 
    {

        final ServerSocket server = new ServerSocket(8080);
        
        System.out.println("Listening for connection on port 8080");

        while (true)
        {
            /*final Socket client = server.accept();

            InputStreamReader input = new InputStreamReader(client.getInputStream());
            BufferedReader reader = new BufferedReader(input);

            String line = reader.readLine();
            while (!line.isEmpty())
            {
                System.out.println(line);
                line = reader.readLine();
            }*/

            try (Socket socket = server.accept())
            {
                Date today = new Date();

                String httpResponse = "HTTP/1.1 200 OK\r\n\r\n" + today;
                socket.getOutputStream().write(httpResponse.getBytes("UTF-8"));
            }
        }


    }

}