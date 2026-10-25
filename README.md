# agent-eval-system
writing an eval system around a refund agent using DeepEval and Langchain

[p.s. I didnt have api tokens so I used my qwen 7B local model connected to langchain local adapter]

## Some words on the project

Project involved in me creating the refund agent, define the tools, the prompts and data[data was extracted from secondary source]/
Writing evals included 7 criterions to cover:
 - answer correctness
 - argument correctness
 - plan adherence
 - plan quality
 - step efficiency
 - task completion
 - tool correctness
   (each has its own test in a .py file)


