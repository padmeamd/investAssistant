package com.investAssistant.investAssistant.util;


import com.investAssistant.investAssistant.DialogState;

public class DialogManager {
    private DialogState currentState = DialogState.START;

    public void handleInput(String input) {
        switch (currentState) {
            case START:
                // Логика начального состояния
                currentState = DialogState.ASK_CRITERIA;
                break;
            case ASK_CRITERIA:
                // Логика получения критериев от пользователя
                currentState = DialogState.ASK_MORE_DETAILS;
                break;
            case ASK_MORE_DETAILS:
                // Логика получения дополнительных деталей
                currentState = DialogState.PROVIDE_RECOMMENDATIONS;
                break;
            case PROVIDE_RECOMMENDATIONS:
                // Логика предоставления рекомендаций
                currentState = DialogState.END;
                break;
            case END:
                // Завершение диалога
                break;
        }
    }

    public DialogState getCurrentState() {
        return currentState;
    }
}
