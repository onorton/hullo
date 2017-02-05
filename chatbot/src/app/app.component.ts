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

  name = ''

  chat_input = ''

  chat = [
    'The birch canoe slid on the smooth planks',
    'Glue the sheet to the dark blue background',
    "It's easy to tell the depth of a well.",
    'These days a chicken leg is a rare dish.',
    'Rice is often served in round bowls.',
    'The juice of lemons makes fine punch.',
    'The box was thrown beside the parked truck.',
    'The hogs were fed chopped corn and garbage.',
    'Four hours of steady work faced us.',
    'Large size in stockings is hard to sell.'
  ]

  constructor(private as: AppService) {}

  ngOnInit() {
  }

  newConvo() {
    this.as.startConversation()
          .subscribe(
            d => console.log(d)
          )
  }

  submitChat(e: any) {
    console.log(e, this.chat_input);
    this.chat.unshift(this.chat_input);
    this.chat_input = '';
  }
}
