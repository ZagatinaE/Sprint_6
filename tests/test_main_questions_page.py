import pytest
import allure
from pages.main_page import MainPage
from data import TestData
from conftest import driver



@allure.feature('Тесты раздела "Вопросы о важном"')
class TestMainQuestion:
    @allure.title('Проверка ответов на вопросы')
    @pytest.mark.parametrize('question_num, expected_answer', TestData.QUESTIONS.items())
    def test_question_answer(self, driver, question_num, expected_answer):
        main_page = MainPage(driver)
        answer = main_page.get_answer_text_after_click(question_num)
        assert answer == expected_answer