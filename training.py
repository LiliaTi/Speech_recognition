import os
import dialogflow
import json


GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')




def create_dialogflow_intent(project_id, intent):
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    response = client.create_intent(parent, intent, language_code='ru')
    return response


def train_dialogflow_agent(project_id):
    client = dialogflow.AgentsClient()
    parent = client.project_path(project_id)
    response = client.train_agent(parent)
    return response


def main():
    project_id = os.environ.get('PROJECT_ID')
    with open('questions.json', 'r', encoding='utf-8') as my_file:
        questions = json.load(my_file)

    intents = []
    for key, value in questions.items():
        training_phrases = []
        for phrase in value['questions']:
            training_phrases.append({"parts": [{"text": phrase}]})
        intent = {
            "display_name": key,
            "messages": [{
                "text":
                {"text": [value['answer']]}
            }],
            "training_phrases": training_phrases
        }
        intents.append(intent)

    for intent in intents:
        create_dialogflow_intent(project_id, intent)

    train_dialogflow_agent(project_id)


if __name__ == '__main__':
    main()
