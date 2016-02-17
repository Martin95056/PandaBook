package my.implementation;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Producer extends Thread {

	private FileOperator visitor;
	private FileHolder fileHolder;
	private Path start;

	public Producer(FileHolder fileHolder, Path path) {
		this.fileHolder = fileHolder;
		this.start = path;
		visitor = new FileOperator(fileHolder);
	}

	@Override
	public void run() {
		synchronized (fileHolder) {
			try {
				Files.walkFileTree(start, visitor);
				fileHolder.setFinished();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}