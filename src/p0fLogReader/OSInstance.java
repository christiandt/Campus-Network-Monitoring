package p0fLogReader;

import java.io.Serializable;
import java.util.HashSet;

public class OSInstance implements Serializable{
	
	private String osName;
	private HashSet<String> ipSet;
	private String macAddress;
	private HashSet<String> usedIpSet;		//used for verifying whether this is an actual unique 
	
	public OSInstance(){
		osName = "null";
		ipSet = new HashSet<String>();
		usedIpSet = new HashSet<String>();
	}
	
	public String getOSName() {
		return osName;
	}
	public void setOSName(String name) {
		this.osName = name;
	}
	public HashSet<String> getIpSet() {
		return ipSet;
	}
	public String getMacAddress() {
		return macAddress;
	}
	public void setMacAddress(String macAddress) {
		this.macAddress = macAddress;
	}

	public HashSet<String> getUsedIpSet() {
		return usedIpSet;
	}
	
	

}
