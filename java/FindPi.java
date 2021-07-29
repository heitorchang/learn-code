public class FindPi {
// HTTPS chat devin's interview question
	public static void main(String[] args) {
		/* Pi, the mathematical constant, can be approximately calculated with the following formula: pi  = 4 * (1 - 1/3 + 1/5 - 1/7 + ...).
		   Write a program that calculates pi out to 5 significant figures using the formula above. Once the calculation is complete, print out the
		   matching pi calculation as well as the last divisor used to calculate the right side of the equation. */
		calcPi();
	}
	private static void calcPi() {
		String piToFive = String.valueOf(Math.PI).substring(0, 7);
		double rightCalcDivisor = 1D;
		double rightSideOfPiCalc = 1D;
		boolean plusCalculation = false;
		for (int i = 1; true; i++) {
			double newPiCalc = 4D * rightSideOfPiCalc;
			String newPiCalcString = String.valueOf(newPiCalc);
			if (newPiCalcString.length() > 6 && newPiCalcString.substring(0, 7).equals(piToFive)) {
				System.out.println("Eureka, pi matches after " + i + " iterations with a divisor of " + rightCalcDivisor);
				System.out.println("Pi to 5 places is " + piToFive);
				System.out.println("Last Pi calculation is " + newPiCalc);
				break;
			}
			rightCalcDivisor += 2;
			rightSideOfPiCalc = plusCalculation ? rightSideOfPiCalc + (1D / rightCalcDivisor) : rightSideOfPiCalc - (1D / rightCalcDivisor);
			plusCalculation = plusCalculation ? false : true;
		}
	}
}
