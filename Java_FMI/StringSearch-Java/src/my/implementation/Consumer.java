package my.implementation;

public class Consumer extends Thread {

	private static String keyword;
	private FileHolder fileHolder;

	public Consumer(FileHolder fileHolder) {
		this.fileHolder = fileHolder;
	}

	public static void setKeyword(String key) {
		keyword = key;
	}

	public static String getKeyword() {
		return keyword;
	}

	@Override
	public void run() {
		synchronized (fileHolder) {

			while (!fileHolder.isProducingFinished() || !fileHolder.isEmpty()) {
				Line data = fileHolder.get();
				if (data.getLine().contains(keyword)) {
					System.out.println(data.toString());
				}
			}
		}
	}
}