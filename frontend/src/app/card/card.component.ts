import { Component, OnInit } from "@angular/core";

@Component({
    selector:'app-card',
    templateUrl: './card.component.html',
    styleUrls: ['./card.component.scss']
})
export class CardComponent implements OnInit{
    title = "Корги";
    text = "Сайт про Корги";
    number = 42;
    array = [0,0,0,0,0]
    obj = {name:"Артем"}
    message:string=""
    imgUrl: string ='https://upload.wikimedia.org/wikipedia/ru/a/a8/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D1%8B%D0%B5_%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B_%D0%9F%D1%80%D0%BE%D0%B1%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B8%D0%BB%D1%8B.jpg';
    newImgUrl:string='https://lifehacker.ru/wp-content/uploads/2020/03/Corgi_1583857179.jpg';
    ngOnInit(){
        setTimeout(()=>{
            this.imgUrl=this.newImgUrl;
        },3000)
    }
    getInfo(){
        return 'This is my info'
    }
    changeImg(){
        this.imgUrl='https://cs8.pikabu.ru/images/big_size_comm/2016-02_5/1456334083194269331.jpg';
    }
    inputHandler(event:any){this.message=event.data}
}