interface Email {
  value: string; // Enforce email format validation
}

interface SecureString {
  value: string;
  isStrong: boolean; // Indicator for password strength
  isLongEnough(minLength: number): boolean; // Method to check if the password meets minimum length requirement
  containsSpecialCharacters(): boolean; // Method to check if the password contains special characters
  containsNumbers(): boolean; // Method to check if the password contains numbers
  containsUppercaseLetters(): boolean; // Method to check if the password contains uppercase letters
}

interface HashedPassword {
  algorithm: string;
  value: string;
}

function login(credentials: { username: Email; password: SecureString }): boolean {
  if (!credentials.password.isStrong) {
    throw new Error("Weak password. Please use a stronger password.");
  }
  
  const hashedPassword: HashedPassword = secureHashPassword(credentials.password.value);
  // ... (code with explicit type checks for security-sensitive operations)
}

function secureHashPassword(password: string): HashedPassword {
  // Implementation of secure password hashing algorithm
  return {
    algorithm: "bcrypt", // Example hashing algorithm
    value: "hashedPasswordValue" // Example hashed password value
  };
}

// Implementation of SecureString methods
function isLongEnough(this: SecureString, minLength: number): boolean {
  return this.value.length >= minLength;
}

function containsSpecialCharacters(this: SecureString): boolean {
  const specialCharactersRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
  return specialCharactersRegex.test(this.value);
}

function containsNumbers(this: SecureString): boolean {
  const numbersRegex = /[0-9]/;
  return numbersRegex.test(this.value);
}

function containsUppercaseLetters(this: SecureString): boolean {
  const uppercaseRegex = /[A-Z]/;
  return uppercaseRegex.test(this.value);
}

// Adding methods to SecureString prototype
(SecureString as any).prototype.isLongEnough = isLongEnough;
(SecureString as any).prototype.containsSpecialCharacters = containsSpecialCharacters;
(SecureString as any).prototype.containsNumbers = containsNumbers;
(SecureString as any).prototype.containsUppercaseLetters = containsUppercaseLetters;
