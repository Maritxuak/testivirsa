import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def write_msg(user_id, message):
    vk_api = vk.get_api() 
    vk_api.messages.send(
        user_id=user_id,
        message=message,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard()
    )

token = ""
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Оставить заявку', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Вакансии', color=VkKeyboardColor.SECONDARY)
keyboard.add_line()
keyboard.add_button('Портфолио', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Сделать заказ', color=VkKeyboardColor.SECONDARY)

def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)

def get_keyboard1():
    
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Обратная связь', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Вакансии', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Портфолио', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Сделать заказ', color=VkKeyboardColor.SECONDARY)
  
    return keyboard.get_keyboard()


def get_keyboard2():
  
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Жалоба', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Предложение', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Вопрос', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Отзыв', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Главная', color=VkKeyboardColor.NEGATIVE)

    
    return keyboard.get_keyboard()

def get_keyboard3():
  
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(label='Менеджер по работе с клиентами', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Главная', color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()

def get_keyboard4():
  
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_callback_button(label='Оставить заявку', color=VkKeyboardColor.POSITIVE, payload={"type": "show_snackbar", "text": "Ваша заявка оставлена! Мы свяжемся с вами в ближайщее время"})
    keyboard.add_line()
    keyboard.add_button('Главная', color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()


keyboard1 = get_keyboard1()
keyboard2 = get_keyboard2()
keyboard3 = get_keyboard3()
keyboard4 = get_keyboard4()

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text
            if request == "Главная":
                    vk_api = vk.get_api() 
                    vk_api.messages.send(
                    peer_id=event.user_id,
                    message='Что вы хотите?',
                    keyboard=keyboard1,
                    random_id=get_random_id()
                    )

            elif request == "Обратная связь":
                    vk_api = vk.get_api() 
                    vk_api.messages.send(
                    peer_id=event.user_id,
                    message='Выберите нужную категорию',
                    keyboard=keyboard2,
                    random_id=get_random_id()
                    )

            elif request == "Вакансии":
                    vk_api = vk.get_api() 
                    vk_api.messages.send(
                    peer_id=event.user_id,
                    message='Актуальные вакансии:',
                    keyboard=keyboard3,
                    random_id=get_random_id()
                    )
            elif request == "Менеджер по работе с клиентами":
                    vk_api = vk.get_api() 
                    message = 'Новое и довольно актуальное предложение:\n\n' \
                              'Нам нужны люди, которые будут находить клиентов.' \
                              'Если у вас уже есть в этом опыт, то это замечательно! \n\n' \
                              'А если опыта нету, то придется обучаться 🙂\n\n' \
                              'И так, вы ищете клиентов. Есть разные варианты для поиска клиентов, например: Биржа фриланса, Kwork.ru, fl.ru и тд.\n\n' \
                              'Также можете находить компании, сообщества которым возможно нужны наши услуги и предлагать им это. К примеру: Есть группа вк, которой возможно нужен бот, ваше дело - предложить им!\n\n' \
                              'Если вы находите клиента, то мы отдаем вам 20% от заказа, после его оплаты.\n\n' \
                              'Чем больше нашли заказов - тем больше получили денег. Все очень просто!\n\n' \
                              'На данный момент мы занимаемся разработкой сайтов на HTML , CSS , REACT , BOOTSTRAP. Также программируем ботов на Python для telegram и VKontakte.\n\n' \
                              'Надеемся, что все очень понятно.\n\n' \
                              'В противном случае мы поможем вам разобраться в вышеперечисленном.\n\n' \
                              'Заинтересовало?🤔\n\n' \
                              'Жми кнопку - "Оставить заявку" и мы обязательно с вами свяжемся! 😉\n\n' 
                    vk_api.messages.send(
                    peer_id=event.user_id,
                    message=message,
                    keyboard=keyboard4,
                    random_id=get_random_id()
                    )
            elif request == "Оставить заявку":
                    vk_api = vk.get_api() 
                    vk_api.messages.send(
                    peer_id=event.user_id,
                    keyboard=keyboard4,
                    random_id=get_random_id(),
                    payload={"type": "show_snackbar", "text": "Ваша заявка оставлена! Мы свяжемся с вами в ближайшее время."}
                    )
            else:
                write_msg(event.user_id, "Не понял вашего ответа...")


