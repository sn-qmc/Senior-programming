// Submission for internal assessment computer science, International Baccalaureatte
// Author: Evelyn O'Brien
// Date: 25/10/2025
// Project name: Cooking Converter
// Code provides user with a client (6 options) to convert ingredients into the desired measurement

package com;
// Import libraries
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileWriter;

public class IA {
    public static void main(String args[]) {
        System.out.println("Program start: Cooking Converter");
        // Create constant and home page
        boolean isReturnToHomePage = true;
        Scanner homePage = new Scanner(System.in);
        Scanner weightConverterPage = new Scanner(System.in);
        Scanner temperatureConverterPage = new Scanner(System.in);
        Scanner volumeConverterPage = new Scanner(System.in);

        // Check if recent.txt file exists or create it
        try {
            File recent = new File("recent.txt");
            if (recent.createNewFile()) {
                System.out.println(recent.getName() + " created.");
            } else {
                System.out.println("recent.txt already exists.");
            }
        } catch (IOException e) {
            System.out.println("Error creating file");
            e.printStackTrace();
        }

        // Main program loop
        while (isReturnToHomePage) {
            int pageNumber = 0;

            // Ask user for menu choice with input validation
            while (true) {
                System.out.println("\nWelcome to Cooking Converter! Please enter the number for one of the pages below");
                System.out.print("""
                        1 - Weight converter
                        2 - Volume converter
                        3 - Temperature converter
                        4 - Recently done conversions                
                        """);
                if (homePage.hasNextInt()) {
                    pageNumber = homePage.nextInt();
                    if (pageNumber >= 0 && pageNumber <= 4) break; // User choice is valid
                    else System.out.println("Invalid option! Please enter a number between 1 and 4."); 
                } else {
                    System.out.println("Invalid input! Please enter a number.");
                    homePage.next(); // Clear invalid input
                }
            }
            // This code block determines the behaviour of each page
            switch (pageNumber) {
                case 1 -> {
                    // Weight converter
                    boolean doAnotherConversion = true;
                    
                    //measurement options for weight
                    while (doAnotherConversion) {
                        System.out.println(""" 
                                \nWeight measurements:
                                grams 
                                milligrams
                                kilograms
                                ounces
                                pounds,
                                cups_flour
                                cups_sugar
                                cups_cocoa_powder
                                cups_cornstarch           
                                tablespoons_flour
                                tablespoons_sugar                             
                                tablespoons_cocoa_powder
                                tablespoons_cornstarch
                                teaspoons_flour
                                teaspoons_sugar                   
                                teaspoons_icing_sugar
                                teaspoons_cocoa_powder
                                teaspoons_cornstarch
                                teaspoons_baking_powder
                                teaspoons_baking_soda
                                teaspoons_salt
                                """);
                        // Check user input is valid
                        double valueToConvert = 0;
                        while (true) {
                            System.out.println("Enter positive value to convert: ");
                            if (weightConverterPage.hasNextDouble()) {
                                valueToConvert = weightConverterPage.nextDouble();
                                break;
                            } else if (valueToConvert <= 0){
                                System.out.println("Invalid number! Please enter a positive number.");
                                weightConverterPage.next();
                            } else{
                                System.out.println("Invalid number! Try again."); //if value inputed isn't valid
                                weightConverterPage.next();
                            }
                        }
                        // User enters unit to convert from
                        System.out.println("Enter unit to convert from (must be unit from list above): ");
                        String unitToConvertFrom = weightConverterPage.next().toLowerCase();
                        // User enters unit to convert to
                        System.out.println("Enter unit to convert to (must be unit from list above): ");
                        String unitToConvertTo = weightConverterPage.next().toLowerCase();

                        // Validate units
                        if (!unitToConvertFrom.matches("pounds|grams|milligrams|kilograms|ounces|cups_flour|cups_sugar|cups_cocoa_powder|cups_cornstarch|tablespoons_flour|tablespoons_sugar|tablespoons_cocoa_powder|tablespoons_cornstarch|teaspoons_flour|teaspoons_sugar|teaspoons_cocoa_powder|teaspoons_cornstarch|teaspoons_baking_powder|teaspoons_baking_soda|teaspoons_salt") ||
                            !unitToConvertTo.matches("pounds|grams|milligrams|kilograms|ounces|cups_flour|cups_sugar|cups_cocoa_powder|cups_cornstarch|tablespoons_flour|tablespoons_sugar|tablespoons_cocoa_powder|tablespoons_cornstarch|teaspoons_flour|teaspoons_sugar|teaspoons_brown_sugar|teaspoons_icing_sugar|teaspoons_cocoa_powder|teaspoons_cornstarch|teaspoons_baking_powder|teaspoons_baking_soda|teaspoons_salt")) {
                            System.out.println("Unidentified measurement unit! Try again.");
                            continue;
                        }

                        // Convert 'from' user input. Conversions are based on pounds
                        double weightMeasurementValues = switch (unitToConvertFrom) {
                            case "pounds" -> valueToConvert;
                            case "grams" -> valueToConvert / 453.6;
                            case "milligrams" -> valueToConvert / 453600;
                            case "kilograms" -> valueToConvert * 2.205;
                            case "ounces" -> valueToConvert / 16;
                            case "cups_flour" -> valueToConvert / 3.6;
                            case "cups_sugar" -> valueToConvert / 2.267962;
                            case "cups_cocoa_powder" -> valueToConvert / 3.84;
                            case "cups_cornstarch" -> valueToConvert / 3.8;                         
                            case "tablespoons_flour" -> valueToConvert / 58.059823;
                            case "tablespoons_sugar" -> valueToConvert / 36.28739;
                            case "tablespoons_cocoa_powder" -> valueToConvert / 0.016;
                            case "tablespoons_cornstarch" -> valueToConvert / 0.017;
                            case "teaspoons_flour" -> valueToConvert / 0.005741;
                            case "teaspoons_sugar" -> valueToConvert / 0.009186;
                            case "teaspoons_cocoa_powder" -> valueToConvert / 0.0054;
                            case "teaspoons_cornstarch" -> valueToConvert / 92.0267;
                            case "teaspoons_baking_powder" -> valueToConvert / 92.03;
                            case "teaspoons_baking_soda" -> valueToConvert / 92.0267;
                            case "teaspoons_salt" -> valueToConvert / 76;
                            default -> valueToConvert; // Default should never be used because user must input one of the units above
                        };

                        // Convert 'to' user input. Conversions are based on pounds
                        double conversionResult = switch (unitToConvertTo) {
                            case "pounds" -> weightMeasurementValues;
                            case "grams" -> weightMeasurementValues * 453.6;
                            case "milligrams" -> weightMeasurementValues * 453600;
                            case "kilograms" -> weightMeasurementValues / 2.205;
                            case "ounces" -> weightMeasurementValues * 16;
                            case "cups_flour" -> weightMeasurementValues * 3.6;
                            case "cups_sugar" -> weightMeasurementValues * 2.267962;
                            case "cups_cocoa_powder" -> weightMeasurementValues * 3.84;
                            case "cups_cornstarch" -> weightMeasurementValues * 3.8;                           
                            case "tablespoons_flour" -> weightMeasurementValues * 58.059823;
                            case "tablespoons_sugar" -> weightMeasurementValues * 36.28739;
                            case "tablespoons_cocoa_powder" -> weightMeasurementValues * 0.016;  
                            case "tablespoons_cornstarch" -> weightMeasurementValues * 0.017;
                            case "teaspoons_flour" -> weightMeasurementValues * 0.005741;
                            case "teaspoons_sugar" -> weightMeasurementValues * 0.009186;
                            case "teaspoons_cocoa_powder" -> weightMeasurementValues * 0.0054;
                            case "teaspoons_cornstarch" -> weightMeasurementValues * 92.0267;
                            case "teaspoons_baking_powder" -> weightMeasurementValues * 92.03;
                            case "teaspoons_baking_soda" -> weightMeasurementValues * 92.0267;
                            case "teaspoons_salt" -> weightMeasurementValues * 76;
                            default -> weightMeasurementValues; // Default should never be used because user must input one of the units above
                        };

                        System.out.printf("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo); // Prints conversion

                        // Save to recent.txt
                        try (FileWriter myWriter = new FileWriter("recent.txt", true)) {
                            myWriter.write(String.format("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo)); // Writes into recent.txt
                        } catch (IOException e) {
                            System.out.println("Unable to write to recent.txt.");
                            e.printStackTrace();
                        }

                        // Ask if user wants to input another weight (continue on this page)
                        System.out.println("Convert another weight? (yes/no): ");
                        String convertAgain = weightConverterPage.next().toLowerCase();
                        if (convertAgain.equals("no")) {doAnotherConversion = false;    
                                            
                    }
                }
            }
                case 2 -> {
                    // Volume converter
                    boolean doAnotherConversion2 = true;
                    

                    while (doAnotherConversion2) {
                        // Options for volume converter
                        System.out.println("""
                                \nLiquid measurements:
                                liquid_ounces
                                millilitres
                                litres
                                pints
                                quarts
                                gallons
                                cups
                                tablespoons
                                teaspoons
                                """);
                        // Check user input is valid
                        double valueToConvert = 0;
                        while (true) {
                            System.out.println("Enter value to convert: ");
                            if (volumeConverterPage.hasNextDouble()) {
                                valueToConvert = volumeConverterPage.nextDouble();
                                break;
                            } else if (valueToConvert <= 0){
                                System.out.println("Invalid number! Please input a positive number");
                                volumeConverterPage.next();                           
                            } else {
                                System.out.println("Invalid number! Try again."); // If value entered is invalid
                                volumeConverterPage.next();
                            }
                        }
                        // User inputs unit to convert from
                        System.out.println("Enter unit to convert from: ");
                        String unitToConvertFrom = volumeConverterPage.next().toLowerCase();
                        // User inputs unit to convert to
                        System.out.println("Enter unit to convert to: ");
                        String unitToConvertTo = volumeConverterPage.next().toLowerCase();

                        // Validate units
                        if (!unitToConvertFrom.matches("liquid_ounces|millilitres|litres|pints|quarts|gallons|cups|tablespoons|teaspoons") ||
                            !unitToConvertTo.matches("liquid_ounces|millilitres|litres|pints|quarts|gallons|cups|tablespoons|teaspoons")) {
                            System.out.println("Unidentified measurement unit! Try again.");
                            continue;
                        }

                        // Convert 'from' user input. Conversions are based on liquid_ounces
                        double volumeMeasurementValues = switch (unitToConvertFrom) {
                            case "liquid_ounces" -> valueToConvert;
                            case "millilitres" -> valueToConvert / 29.574;
                            case "litres" -> valueToConvert * 33.814;
                            case "gallons" -> valueToConvert * 128;
                            case "quarts" -> valueToConvert * 32;
                            case "pints" -> valueToConvert * 16;
                            case "cups" -> valueToConvert * 8;
                            case "tablespoons" -> valueToConvert / 2;
                            case "teaspoons" -> valueToConvert / 6;
                            default -> valueToConvert; // Default should never be used because user must input one of the units above
                        };

                        // Convert 'to' user input. Conversions are based on liquid_ounces
                        double conversionResult = switch (unitToConvertTo) {
                            case "liquid_ounces" -> volumeMeasurementValues;
                            case "millilitres" -> volumeMeasurementValues * 29.574;
                            case "litres" -> volumeMeasurementValues / 33.814;
                            case "gallons" -> volumeMeasurementValues / 128;
                            case "quarts" -> volumeMeasurementValues / 32;
                            case "pints" -> volumeMeasurementValues / 16;
                            case "cups" -> volumeMeasurementValues / 8;
                            case "tablespoons" -> volumeMeasurementValues * 2;
                            case "teaspoons" -> volumeMeasurementValues * 6;
                            default -> volumeMeasurementValues; // Default should never be used because user must input one of the units above
                        };

                        System.out.printf("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo); //Prints conversion

                        // Save to file
                        try (FileWriter myWriter = new FileWriter("recent.txt", true)) {
                            myWriter.write(String.format("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo)); // Writes into recent.txt
                        } catch (IOException e) {
                            System.out.println("Unable to write to recent.txt.");
                            e.printStackTrace();
                        }
                        // Ask if user wants to input another weight (continue on this page)
                        System.out.print("Convert another volume? (yes/no): ");
                        String convertAgain2 = volumeConverterPage.next().toLowerCase();
                        if (!convertAgain2.equals("yes")) doAnotherConversion2 = false;
                    }
                }
                case 3 -> {
                    // Temperature converter
                    boolean doAnotherConversion3 = true;                   
                    // Options for temperature converter
                    while (doAnotherConversion3) {
                        System.out.println("""
                                \nTemperature units:
                                celsius
                                fahrenheit
                                kelvin
                                rankine
                                """);
                        // Check if user input is valid
                        double valueToConvert = 0;
                        while (true) {
                            System.out.println("Enter value to convert: ");
                            if (temperatureConverterPage.hasNextDouble()) {
                                valueToConvert = temperatureConverterPage.nextDouble();
                                break;
                            } else if (valueToConvert <= 0) {
                                System.out.println("Invalid number! Please input a positive number");
                                temperatureConverterPage.next();
                            } else {
                                System.out.println("Invalid number! Try again."); // If value inputed is invalid
                                temperatureConverterPage.next();
                            }
                        }
                        // User inputs unit to convert from
                        System.out.println("Enter unit to convert from: ");
                        String unitToConvertFrom = temperatureConverterPage.next().toLowerCase();
                        // User inputs unit to convert to
                        System.out.println("Enter unit to convert to: ");
                        String unitToConvertTo = temperatureConverterPage.next().toLowerCase();

                        // Validate units
                        if (!unitToConvertFrom.matches("celsius|fahrenheit|kelvin|rankine") ||
                            !unitToConvertTo.matches("celsius|fahrenheit|kelvin|rankine")) {
                            System.out.println("Unidentified measurement unit! Try again.");
                            continue;
                        }

                        double temperatureMeasurementValues = switch (unitToConvertFrom) {
                            case "celsius" -> valueToConvert;
                            case "fahrenheit" -> (valueToConvert - 32) * 5 / 9;
                            case "kelvin" -> valueToConvert - 273.15;
                            case "rankine" -> (valueToConvert - 491.67) * 5 / 9;
                            default -> valueToConvert;
                        };

                        double conversionResult = switch (unitToConvertTo) {
                            case "celsius" -> temperatureMeasurementValues;
                            case "fahrenheit" -> temperatureMeasurementValues * 9 / 5 + 32;
                            case "kelvin" -> temperatureMeasurementValues + 273.15;
                            case "rankine" -> (temperatureMeasurementValues + 273.15) * 9 / 5;
                            default -> temperatureMeasurementValues;
                        };

                        System.out.printf("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo);

                        // Save to file
                        try (FileWriter myWriter = new FileWriter("recent.txt", true)) {
                            myWriter.write(String.format("%.2f %s is equal to %.2f %s%n", valueToConvert, unitToConvertFrom, conversionResult, unitToConvertTo));
                        } catch (IOException e) {
                            System.out.println("Unable to write to recent.txt.");
                            e.printStackTrace();
                        }

                        System.out.println("Convert another temperature? (yes/no): ");
                        String convertAgain3 = temperatureConverterPage.next().toLowerCase();
                        if (!convertAgain3.equals("yes")) doAnotherConversion3 = false;
                    }
                }
                case 4 -> {
                    System.out.println("Recently done conversions:");
                    try {
                        File recent = new File("recent.txt");
                        Scanner myReader = new Scanner(recent);
                        while (myReader.hasNextLine()) {
                            System.out.println(myReader.nextLine());
                        }
                        myReader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("Error reading file.");
                        e.printStackTrace();
                    }
                }
         
            }

            // Ask if user wants to return to main menu
               System.out.println("\nReturn to main menu? (yes/no): ");
                String returnToHome = homePage.next().toLowerCase(); // homepage
                if (returnToHome.equals("no")) {
                    isReturnToHomePage = false;
                    System.out.println("Exiting program. Goodbye!");
                   
                }
            
        }
        weightConverterPage.close();
        volumeConverterPage.close();
        temperatureConverterPage.close();
        homePage.close();
    }
}

