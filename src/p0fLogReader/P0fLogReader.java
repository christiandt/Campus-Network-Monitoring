package p0fLogReader;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Serializable;
import java.util.HashMap;

public class P0fLogReader implements Serializable {

	public void readFingerprints(String pathToLog, HashMap<String, OSInstance> ipMap){
		BufferedReader br;
		String line;
		int ipStart = -1;
		int ipEnd = -1;
		String ip;
		int osNameStartPosition;
		int osNameEndPosition;
		String osName;
		OSInstance os;
		try {
			br = new BufferedReader(new FileReader(pathToLog));
			line = br.readLine();
			while(line != null){
				if(line.contains("mod=mtu") || line.contains("mod=uptime")
						|| line.contains("mod=syn+ack") 
						|| line.contains("mod=http request")
						|| line.contains("mod=http response")){
					line = br.readLine();
					continue;
				}
				ipStart = line.indexOf("cli=") + 4;
				ipEnd = line.indexOf("/", ipStart);
				ip = line.substring(ipStart, ipEnd);
				osNameStartPosition = line.indexOf("os=") + 3;
				osNameEndPosition = line.indexOf('|', osNameStartPosition);
				osName = line.substring(osNameStartPosition, osNameEndPosition);
				if(!ipMap.containsKey(ip)){
					os = new OSInstance();
					os.setOSName(osName);
					os.getIpSet().add(ip);
					ipMap.put(ip,os);
				}
				
				line = br.readLine();
			}
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}


}
