package p0fLogReader;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class OSFingerprinter implements Serializable {
	private String pathToP0fFingerprintsFile;
	private String pathToWorkingDirectory;
	private String textFileName;
	private String textFileEnding;
	private P0fLogReader lr;
	private CapturedTxtReader ct;
	private HashMap<String, OSInstance> macMap;
	private HashMap<String, OSInstance> ipMap;
	private int numberOfTxtFiles; 
	private String osfFileName;
	
	public OSFingerprinter(){
		lr = new P0fLogReader();
		ct = new CapturedTxtReader();
		macMap = new HashMap<String, OSInstance>();
		ipMap = new HashMap<String, OSInstance>();
//		pathToLog = getClass().getClassLoader().getResource(".").getPath() + "test_log.txt";
//		pathToTxtFile = getClass().getClassLoader().getResource(".").getPath() + "test_tcp_only.convertet.txt";
//		pathToLog = getClass().getClassLoader().getResource(".").getPath() + "1.TCP_only_OS_Fingerprinting_log.txt";
//		pathToTxtFile = getClass().getClassLoader().getResource(".").getPath() + "1.TCP_only.txt";
		pathToP0fFingerprintsFile = "tuesday_10.22_OS_fingerprinting_log.txt";
		pathToWorkingDirectory = "/home/chucky/BIG FILES/captures/10.22/tcp_only/";
		
		textFileName = "tuesday_30_min_tcp_only_text_";
		textFileEnding = ".txt";
		numberOfTxtFiles = 5;
		osfFileName = "osf.javaObject";

		
		
	}
	
	
	public static void main(String[] args){
		OSFingerprinter osf = new OSFingerprinter();
		File f = new File(osf.pathToWorkingDirectory+osf.osfFileName);
		if (!f.exists()){
			
			for (int i=1;i<osf.numberOfTxtFiles+1;i++){			//the txt file is spilt so i need to read every one of them.
				osf.ct.readCapturedTxtFile(osf.pathToWorkingDirectory+osf.textFileName+i+osf.textFileEnding, osf.macMap, i);
			}
			//just printing som statistics about the number of mac addresses with more than one ip address
			osf.ct.checkForDuplicateIpAdresses(osf.macMap); 	//probably some of the mac addresses will have more than one ip
			
			//reading the p0f log 
			osf.lr.readFingerprints(osf.pathToWorkingDirectory+osf.pathToP0fFingerprintsFile, osf.ipMap);
			
			//writing the HasMaps to a file (to save time each time i run the program)
			FileOutputStream fout;
			try {
				fout = new FileOutputStream(osf.pathToWorkingDirectory+osf.osfFileName);
				ObjectOutputStream oos = new ObjectOutputStream(fout);
				oos.writeObject(osf);
				oos.close();
			} catch (FileNotFoundException e) {
				System.out.println("File not found, javaObject");
			} catch (IOException e) {
				e.printStackTrace();
			}
			
		}
		else { 		//a file exists and we can read it
			System.out.println("reading saved OSFingerprinting object");
			try {
				FileInputStream fin = new FileInputStream(osf.pathToWorkingDirectory+osf.osfFileName);
				ObjectInputStream ois = new ObjectInputStream(fin);
				osf = (OSFingerprinter) ois.readObject();
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			
		}
		
		//checking for actual unique mac-OS fingerprints
		osf.checkForUniqueOSes(osf.ipMap, osf.macMap);
		
		System.out.println("ipMap.size = "+osf.ipMap.size());
		System.out.println("Finished");
	}
	
	
	
	
	public void checkForUniqueOSes(HashMap<String, OSInstance> ipMap, HashMap<String, OSInstance> macMap){
		System.out.println("");
		Iterator<Entry<String, OSInstance>> macIt = macMap.entrySet().iterator();
		Iterator<Entry<String, OSInstance>> ipIt;
		Map.Entry<String, OSInstance> macEntry;
		Map.Entry<String, OSInstance> ipEntry;
		OSInstance os;
		String macIp = "";
		String ipIp = "";
		int counter = 0;
		while(macIt.hasNext()){
			macEntry = macIt.next();
			ipIt = ipMap.entrySet().iterator();
			while(ipIt.hasNext()){
				ipEntry = ipIt.next();
				if(macEntry.getValue().getIpSet().contains(ipEntry.getKey())){
					os = macEntry.getValue();
					os.setOSName(ipEntry.getValue().getOSName());
					os.getUsedIpSet().add(ipEntry.getKey());
					os.getIpSet().remove(ipEntry.getKey());
					System.out.println("counter = "+counter);
					counter++;
				}
			}
		}
		System.out.println("");
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
}
