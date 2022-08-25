import React from 'react';



function changeSideCart (){
    
}
const CartTourItem = (tours) => {



    return(

            <div className="col center-xs-4">
                <div className="card">
                 
                    <div className="card_front">
                        <a href=""><img className='card-img' src="https://www.zr.ru/d/story/a6/907430/033_20170715_rec-(1).jpg" alt="Фото7 "/></a>
                        <div className='description_block_card'>
                            <p className="card_p1"><span className='cart_word_red'>{tours.post.name}</span></p>
                            <p className="card_p2">Продолжительность {tours.post.duration}</p>
                            <p className="card_p3">{tours.post.price} ₽</p>
                        </div>
                    </div>
               
                    <div className="card_back">
                        <div className='description_back_card'>
                            <p className="card_p1">{tours.post.name}</p>
                            <p className="card_p3">Продолжительность {tours.post.duration}</p>
                            <p className="card_p3">Возраст {tours.post.min_age}+</p>
                            <p className="card_p3">{tours.post.price} ₽ за одного человека</p>
                            <p className="card_p3">Max количество человек {tours.post.number_people}</p>
                            <p className="card_p3">Маршрут:</p>
                            <p className="card_p2">Сопка-Столбы-Набережная Енисея</p>
                        </div>
                    </div>
                </div>
            </div>
    )
};


export default CartTourItem