import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/observable/throw';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/do';  // for debugging

/**
 * This class provides the Query service with methods to read names and add names.
 */
@Injectable()
export class AppService {

  API = 'http://battle.horse:5000';

  /**
   * Creates a new NameListService with the injected Http.
   * @param {Http} http - The injected Http.
   * @constructor
   */
  constructor(private http: Http) {}

  startConversation() : Observable<any> {
    return this.http.get(this.genUri('/conversation'))
                    .map((res:Response) => res.json())
                    .catch(this.handleError);
  }


  getConversation(uid) : Observable<any> {
      return this.http.get(this.genUri('/conversation/' + uid))
                    .map((res:Response) => res.json())
                    .catch(this.handleError);
  }




  postMessageToConversation(uid, query) : Observable<any> {
      let headers = new Headers({"content-type":"application/json"});
      let options = new RequestOptions({headers: headers});
      console.log(query);
      return this.http.post(this.genUri('/conversation/' + uid), JSON.stringify(query), options)
                    .map((res:Response) => res.json())
                    .catch(this.handleError);
  }

  /**
    * Handle HTTP error
    */
  private handleError (error: any) {
    // In a real world app, we might use a remote logging infrastructure
    // We'd also dig deeper into the error to get a better message
    let errMsg = (error.message) ? error.message :
      error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg); // log to console instead
    return Observable.throw(errMsg);
  }

  /**
   * Appends path to API
   * @param {string} path - path to resource
   * @return {string} - full path including server address
   */
  private genUri(path: string, query?: Query[]) : string {
    let uri = this.API + path + (query === undefined ? '' : '?');
    if(query !==undefined) {
      for(let i = 0; i < query.length; i++) {
        uri += ( query[i].name + '=' + query[i].value );
        if( i < query.length - 1 ) {
          uri += '&';
        }
      }
    }
    return uri;
  }
}

interface Query {
  name: string;
  value: any;
}
