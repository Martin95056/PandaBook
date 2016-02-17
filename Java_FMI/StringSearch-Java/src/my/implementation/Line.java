package my.implementation;

public class Line {
	private String infoForFile;
	private String line;

	public String getId() {
		return infoForFile;
	}

	public void setId(String id) {
		this.infoForFile = id;
	}

	public Line(String fileName, long row, String line) {
		this.infoForFile = String.format("File is %s - line is %s", fileName,
				String.valueOf(row));
		this.setLine(line);
	}

	public String getLine() {
		return line;
	}

	public void setLine(String line) {
		this.line = line;
	}

	@Override
	public String toString() {
		return String.format("%s, text: %s", infoForFile, line);
	}

}