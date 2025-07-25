from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from apps.keyboards.default.user import user_main_menu
from apps.states.user import Feedback

router = Router()


@router.message(Feedback.feedback, F.text == "Back ⬅️")
async def back_user_main_menu(message: types.Message, state: FSMContext):
    text = "Main menu"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.clear()