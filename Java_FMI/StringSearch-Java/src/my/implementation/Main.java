package my.implementation;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		Path path = Paths.get("/home/ruzha/eclipse_projects/myProject/Test");
		System.out.print("Please, enter a word: ");
		Scanner userInput = new Scanner(System.in);
		String word = userInput.next();

		Consumer.setKeyword(word);

		int numberOfProducers = 3;
		int numberOfConsumers = 3;

		Thread[] producers = new Thread[numberOfProducers];
		Thread[] consumers = new Thread[numberOfConsumers];

		FileHolder fileHolder = new FileHolder();

		for (int i = 0; i < numberOfConsumers; i++) {
			producers[i] = new Producer(fileHolder, path);
		}

		for (int i = 0; i < numberOfConsumers; i++) {
			consumers[i] = new Consumer(fileHolder);
		}

		for (Thread producer : producers) {
			producer.start();
		}

		for (Thread consumer : consumers) {
			consumer.start();
		}

		for (Thread producer : producers) {
			producer.join();
		}

		for (Thread consumer : consumers) {
			consumer.join();
		}

		userInput.close();
	}

}
