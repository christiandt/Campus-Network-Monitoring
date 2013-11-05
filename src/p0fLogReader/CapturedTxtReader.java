package p0fLogReader;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class CapturedTxtReader implements Serializable {
	
	public void readCapturedTxtFile(String pathToTxtFile, HashMap<String, OSInstance> macMap, int fileNr){
		BufferedReader br;
		String line;
		OSInstance os = null;
		int macStart;
		int macEnd;
		int ipStart;
		int ipEnd;
		int frameNr = 0;
		System.out.println("");
		try {
			br = new BufferedReader(new FileReader(pathToTxtFile));
			line = br.readLine();
			while(line != null){
				if(line.startsWith("Frame ")) {
					frameNr = frameNr+1;
					if(frameNr%10000 == 0)System.out.println("fileNr: "+fileNr+" frameNr: "+frameNr);
					os = new OSInstance();
				}
				else if (line.contains("    Transmitter address: ")){
					macStart = line.indexOf('(') +1 ;
					macEnd = line.indexOf(')');
					os.setMacAddress(line.substring(macStart, macEnd));
				}
				else if (line.startsWith("Internet Protocol")){ //Internet protocol v4 (could it be v6?)
					ipStart = line.indexOf('(') + 1;
					ipEnd = line.indexOf(')');
					os.getIpSet().add(line.substring(ipStart, ipEnd));
					if (!macMap.containsKey(os.getMacAddress())){
						System.out.println(macMap.size());
						macMap.put(os.getMacAddress(), os);			//Storing the os in a map
					}
					else if (!macMap.get(os.getMacAddress()).getIpSet().contains(os.getIpSet())){
						macMap.get(os.getMacAddress()).getIpSet().addAll(os.getIpSet());
					}
				}
				line = br.readLine();
			}
		} catch (FileNotFoundException e) {
			System.out.println("File not found");
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("");
	}
	
	public void checkForDuplicateIpAdresses(HashMap<String, OSInstance> macMap){
		Iterator<Entry<String, OSInstance>> it = macMap.entrySet().iterator();
		Map.Entry<String, OSInstance> entry;
		int counter = 0;
		System.out.println("");
		while(it.hasNext()){
			entry = it.next();
			if(entry.getValue().getIpSet().size()>1){
				System.out.println("counter = "+counter);
				counter++;
				System.out.println("ipSet size = "+entry.getValue().getIpSet().size());
			}
		}
		System.out.println("");
	}

	
	
	
}
