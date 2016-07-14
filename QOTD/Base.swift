//
//  Base.swift
//  QOTD
//
//  Created by Ahmed Musse on 7/13/16.
//  Copyright © 2016 Ahmed Musse. All rights reserved.
//

import Foundation
import Firebase

// Global variables that can be referenced throughout the app

// Database URLs
let BASE_URL = "https://iquotation.firebaseio.com/"
let DB_URL = "https://iquotation.firebaseio.com/quotes"


// Firebase references

let DB_BASE = Firebase(url: BASE_URL)
let DB_REF = Firebase(url: DB_URL)

//var CURRENT_USER: Firebase
//{
//    let userID = NSUserDefaults.standardUserDefaults().valueForKey("uid") as! String
//    let currentUser = Firebase(url: "\(DB_REF)").childByAppendingPath("users").childByAppendingPath(userID)
//    return currentUser!
//}