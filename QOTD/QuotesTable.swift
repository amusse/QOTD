//
//  ViewController.swift
//  QOTD
//
//  Created by Ahmed Musse on 7/9/16.
//  Copyright © 2016 Ahmed Musse. All rights reserved.
//

import UIKit
import Firebase

class QuotesTable: UIViewController, UITableViewDataSource, UITableViewDelegate {

    @IBOutlet weak var tableView: UITableView!
    let CellName         = "QuoteCell"
    var quotes = NSDictionary()
    var authors = [String]();
    var quotesText = [String]();
    var topics = [String]();

    override func viewDidLoad() {
        super.viewDidLoad()
        
        getQuotes()
        tableView.delegate = self

    }
    
    func getQuotes() {
        // Get all the Favorites of current user
        DB_REF.observeSingleEventOfType(.Value, withBlock: {
            shot in
            self.quotes = shot.value as! NSDictionary
            
            let allQuotes = shot.value as! [String:NSDictionary]
            for (_, details) in allQuotes {
                self.authors.append(details["author"] as! String)
                self.quotesText.append(details["quote"] as! String)
                let topic = details["topics"] as! [String]
                var topicsText = ""
                for word in topic {
                    topicsText = topicsText + word + ", ";
                }
                topicsText = topicsText[topicsText.startIndex.advancedBy(0)...topicsText.startIndex.advancedBy(topicsText.characters.count - 3)]
                //"Strin"
                self.topics.append(topicsText);
            }
            self.tableView.reloadData();
        })
    }
    
    func createNotif(date: NSDate) {
        let rand = Int(arc4random_uniform(UInt32(authors.count)) + 1)
        let randomQuote = quotesText[rand];
        let author = authors[rand];
        
        let text = randomQuote + " - " + author;
        let localNotification = UILocalNotification();
        localNotification.fireDate = date;
        localNotification.soundName = UILocalNotificationDefaultSoundName
        localNotification.alertBody = text;
        UIApplication.sharedApplication().scheduleLocalNotification(localNotification)
    }
    
    @IBAction func btnBeginNotifications(sender: AnyObject) {
        
        createNotif(NSDate().dateByAddingTimeInterval(30));
        createNotif(NSDate().dateByAddingTimeInterval(30));
        createNotif(NSDate().dateByAddingTimeInterval(7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(24 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(24 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(24 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(48 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(48 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(48 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(72 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(72 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(72 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(96 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(96 * 7 * 60 * 60));
        createNotif(NSDate().dateByAddingTimeInterval(96 * 7 * 60 * 60));
        let alertController = UIAlertController(
            title: "Notifications Added!",
            message: "You will now get notified with daily quotes for the week. Enjoy!",
            preferredStyle: .Alert);
        
        alertController.addAction(UIAlertAction(title: "OK",
            style: UIAlertActionStyle.Default, handler: nil));
        presentViewController(alertController, animated: true, completion: nil);
        
        
    }
    func tableView(tableView: UITableView,
        numberOfRowsInSection section: Int) -> Int {
            return authors.count
    }

    func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        let row = indexPath.row
        let section = indexPath.section
        tableView.deselectRowAtIndexPath(indexPath, animated: true)
//        self.performSegueWithIdentifier("toFavDetails", sender: self)
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier(CellName) as! QuoteCell
        let section = indexPath.section
        let row = indexPath.row
        cell.tvQuote.text = quotesText[row];
        cell.lAuthor.text = authors[row];
        cell.lTopic.text = topics[row];
        
        return cell
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {

    }
    
    
    



}

