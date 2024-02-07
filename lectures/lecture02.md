# Lecture 2 - Feb. 7, 2024

## Housekeeping

## Notes
Using Formal Methods with Type Theory, Specification, and Testing for Large Language Models (LLMs)
Integrating formal methods with type theory, specification, and testing offers exciting possibilities for improving the development and reliability of LLMs. Here's how they can be used together:

1. Type Theory:

Formal type systems: Specify precise interfaces for LLMs, defining acceptable inputs, outputs, and behaviors. This can catch errors early in development and ensure type safety, crucial for preventing unexpected outputs.
Theorem proving: Prove properties about LLM code using mathematical logic, guaranteeing correctness under certain conditions. This is particularly valuable for safety-critical applications of LLMs like code generation or medical diagnosis.
Dependent types: Link types and values, allowing dynamic checks based on input data. This can enforce specific constraints on LLM outputs depending on the input, enhancing data-driven correctness.

2. Specification:

Formal specifications: Clearly define the intended behavior of the LLM using languages like Z or TLA+. This serves as a reference point for development, testing, and verification.
Model checking: Verify if the LLM implementation adheres to the formal specification using automated tools. This helps identify potential inconsistencies between design and implementation.
Contract-based programming: Specify expectations for LLM inputs and outputs as contracts. These contracts can be automatically checked during training and usage, improving robustness.

3. Testing:

Symbolic execution: Explore all possible execution paths of the LLM code symbolically, identifying potential corner cases and vulnerabilities. This is especially useful for uncovering edge cases that traditional testing might miss.
Property-based testing: Generate test cases based on desired properties of the LLM, ensuring diverse and relevant testing coverage. This helps uncover hidden biases and unexpected outputs.
Fuzz testing: Feed the LLM with random or malformed inputs to test its robustness and resilience to unexpected data. This helps identify potential security vulnerabilities and data handling issues.
Challenges and Opportunities:

Integrating these methods with LLMs presents challenges:

Complexity: LLMs are inherently complex, making formalization and verification non-trivial.
Scalability: Applying formal methods across large LLM architectures can be computationally expensive.
Evolving nature: LLMs are constantly learning and evolving, making verification a moving target.
Despite these challenges, the potential benefits are significant:

Enhanced reliability: Formal methods can significantly reduce errors and guarantee certain correctness properties.
Improved transparency: Formal specifications and proofs can make LLM behavior more understandable and interpretable.
Safer applications: Formal methods can mitigate risks associated with deploying LLMs in critical applications.
Overall, the combination of formal methods with type theory, specification, and testing holds immense promise for creating more reliable, robust, and trustworthy LLMs. As research in this area progresses, we can expect significant advancements in the development and deployment of these powerful language models.

4. Integrating Software Toolchains

Tools such as git help in backtracking. With coding assistance, being able to track previously working revisions of code is key. Using linters is also critical because LLMs do not always produce syntantically or semantically correct code. 


## For Lecture
- Testing use of Discord
- Chat-GPT 4 use of Aider & OpenAI
- Notes and assignments on GitHub
- GitHub centric problems

## Homework
- hook into Discord (instructions to be provided via Discord)
- 

## Other Details:
- IDE: VS Code or Vim preferred
- NixOS
- Discord for Communication

## References:
