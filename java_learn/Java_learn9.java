package java_learn;

public class Java_learn9 {
	public static void main(String[] args) {
	Person str = new Student();
	Person tec = new Teacher();

	str.run();
	tec.run();
	}
}

class Person {
	private String name;
	private int age;

	public void run() {
		System.out.println("Person.run");
	}
}

class Student extends Person {
	private int score;
	
	@Override
	public void run() {
		System.out.println("Student.run");
	}
}

class Teacher extends Person {
	@Override
	public void run() {
		System.out.println("Teacher.run");
	}
}

