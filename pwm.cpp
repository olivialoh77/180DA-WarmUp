



/*
 * author: Eric Tang 2020
 */
#include "stm32f4xx_hal.h"
#include "pwm.h"

//TO DO: Put all timer sources in class initialization. Add private variables where needed.
PWM::PWM(TIM_HandleTypeDef* htim_2, TIM_HandleTypeDef* htim_3):m_htim_2(htim_2),m_htim_3(htim_3){
}

//TO DO: Change channels and timer ports for HAL_TIM_PWM_Start
void PWM::start(){
	HAL_TIM_PWM_Start(m_htim_2, TIM_CHANNEL_1);
	//HAL_TIM_PWM_Start(m_htim_3, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(m_htim_3, TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(m_htim_3, TIM_CHANNEL_3);
}

//TO DO: Change which timer port you use and also which channel to use. CCRx is for channel x.
void PWM::setduty(uint8_t duty1, uint8_t duty2, uint8_t duty3, uint8_t duty4){
	(*m_htim_2).Instance->CCR1 = duty1;
	//(*m_htim_3).Instance->CCR1 = duty2;
	(*m_htim_3).Instance->CCR2 = duty3;
	(*m_htim_3).Instance->CCR3 = duty4;
}


