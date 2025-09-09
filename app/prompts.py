from fastapi import APIRouter, HTTPException
from typing import Any
from app.models import Query, QuestionType
from llama_cpp import Llama
from langchain.prompts import PromptTemplate

router = APIRouter()

model_path = './app/model.gguf'

llm = Llama(
    model_path=model_path,
    n_ctx=0,
    n_threads=4, 
    verbose=False
)

locate_template = """
Which country is {search} in? 
"""

about_template = """
Tell me about {search}:
"""

meaning_template = """
What does "{search}" mean?: 
"""

locate_prompt = PromptTemplate(input_variables=["search"], template=locate_template)
similar_word_prompt = PromptTemplate(input_variables=["search"], template=meaning_template)
meaning_prompt = PromptTemplate(input_variables=["search"], template=meaning_template)

@router.post('/prompt')
def process_prompt(query: Query) -> dict[str, Any]:

    prompt = None
    if query.questionType == QuestionType.LOCATE:
        prompt = locate_prompt.format(search=query.searchItem)
    elif  query.questionType == QuestionType.MEANING:
        prompt = meaning_prompt.format(search=query.searchItem)
    else:
        prompt = about_template.format(search=query.searchItem)

    output = llm(prompt, max_tokens=256, temperature=0.2, stop=['.'])
    llm.reset()

    strResponse = output["choices"][0]["text"].strip().split('.')[0]
    
    return {"response": strResponse}