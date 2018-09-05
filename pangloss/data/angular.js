// Use text-mode

var data = [

/*
    { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },
*/

  { // begin new topic
    topic: 'Services',
    title: 'AngularFire2 data',
    reference: '',
    description: `
    Each collection of data should have its own service.
      `,
    code: `
ng generate service settings --module=app

// app/settings.service.ts

import { Injectable } from '@angular/core';
import { Transaction } from './transaction';
import { TRANSACTIONS } from './mock-transactions';

import { AngularFirestore } from 'angularfire2/firestore';
import {Observable} from 'rxjs/Observable';
import * as firebase from 'firebase/app';

@Injectable()
export class SettingsService {

  constructor() { }

  getSettings(db: AngularFirestore, user: firebase.User): Observable<any> {
    if (user) {
      let userDoc = db.doc('users/' + user.uid);
      return userDoc.valueChanges();
    } else {
      return Observable.of();
    }
  }

}

    `
  },

  { // begin new topic
    topic: 'Services',
    title: 'async retrieval',
    reference: '',
    description: `Given an observable, get its value`,
    code: `
this.afAuth.authState.subscribe(user => this.loadData(user));    
    `
  },

  { // begin new topic
    topic: 'Services',
    title: 'Chain of observables (foreign key)',
    reference: '',
    description: ``,
    code: `
  getBaseCurrency(db: AngularFirestore, user: firebase.User): Observable<any> {
    if (user) {
      let userDoc = db.doc('/users/' + user.uid);
      let userSource = userDoc.valueChanges();

      return userSource.switchMap(data => {
        let path = '/users/' + user.uid + '/currencies/' + data.baseCurrency.id;
        return db.doc(path).valueChanges();
      });
      
    } else {
      return Observable.of({
        'name': 'No User Currency'
      });
    }
  }
    
    `
  },


  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

];

