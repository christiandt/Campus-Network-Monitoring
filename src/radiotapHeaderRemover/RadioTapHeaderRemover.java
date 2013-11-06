package radiotapHeaderRemover;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public class RadioTapHeaderRemover {
	private String workingDir;
	private String filename;
	
	
	public RadioTapHeaderRemover(){
		workingDir = "/home/chucky/BIG FILES/captures/10.21/";
		filename = "test_tcp shortened.txt";
//		filename = "test.txt";
		
	}
	
	public static void main(String[] args){
		RadioTapHeaderRemover rr = new RadioTapHeaderRemover();
		
		rr.removeRadioTapHeader(rr.workingDir, rr.filename);
	
		
	}
	
	public void removeRadioTapHeader(String workingDir, String filename){
		
		
		
		try {
			File readFile = new File(workingDir+filename);
			File writeFile = new File(workingDir+"edited"+filename);
			BufferedReader br = new BufferedReader(new FileReader(readFile));
			BufferedWriter bw = new BufferedWriter(new FileWriter(writeFile));
			String line = br.readLine();	
			boolean skipLine = false;
			while(line != null){
				if (line.startsWith("Radiotap Header")){
					skipLine = true;
				}
				else if (line.startsWith("    Antenna:")){
					skipLine = false;
				}
				else if (skipLine){
				}
				
				else{
					bw.write(line);
					bw.newLine();
				}
				line = br.readLine();
			}
			bw.close();
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
