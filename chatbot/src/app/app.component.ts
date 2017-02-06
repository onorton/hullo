import { Component, AfterViewInit, OnInit } from '@angular/core';
import { MdDialog, MdToolbar, MdDialogRef, MdSnackBar} from '@angular/material';
import { AppService } from './app.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Hullo Clever Chatbot!';

  people = ['Blaine Rogers', 'Shakespeare', 'Mickey Mouse']

  name = 'Bob';

  chat_input = '';

  chat = []; 

  convo_id = 0;

  constructor(private as: AppService) {}

  ngOnInit() {
    // setInterval(() => 
    //   this.getConvo(this.convo_id), 5000
    // );
    this.getConvo(this.convo_id);
  }

  nextPerson() {
    this.convo_id+=1;
    this.getConvo(this.convo_id);
  }

  previousPerson() {
    this.convo_id-=1;
    this.getConvo(this.convo_id)
  }

  newConvo() {
    this.as.startConversation()
          .subscribe(
            d => { 
              console.log(d)
              this.convo_id = d;
              this.getConvo(d);
            }
          )
  }

  getConvo(id) {
    this.as.getConversation(id)
          .subscribe(
            d => {
              this.chat = d;
              console.log(this.chat)
            },
            error => {
              this.newConvo()
            }
          )
  }

  submitChat(e: any) {
    if(this.chat_input == '') {
      return;
    }

    let chatJson = {
      "message_id" : this.chat.length,
      "sender" : this.name,
      "time" : Math.floor((new Date()).getTime() / 1000),
      "content" : this.chat_input
    }
    this.chat.unshift(chatJson);
    this.as.postMessageToConversation(this.convo_id, chatJson)
            .subscribe(
                d => {
                  this.chat.unshift(d);
                }
            )
    this.chat_input = '';
    // this.getConvo(this.convo_id);
  }
}
