import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { AppComponent, DialogDialog } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    DialogDialog
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule.forRoot()
  ],
  entryComponents: [DialogDialog],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
