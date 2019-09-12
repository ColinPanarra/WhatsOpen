package com.example.whatsopen;
/*
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import com.firebase.ui.database.FirebaseListAdapter;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.lang.reflect.Array;
import java.text.DateFormat;
import java.util.ArrayList;
import java.util.Map;
public class MainActivity extends AppCompatActivity {

    // ...

    private ListView mListView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Find the ListView
        mListView = (ListView) findViewById(R.id.list);

        /*
         * Create a DatabaseReference to the data; works with standard DatabaseReference methods
         * like limitToLast() and etc.
         */
        DatabaseReference storesReference = FirebaseDatabase.getInstance().getReference()
                .child("stores");

        // Now set the adapter with a given layout
        mListView.setAdapter(new FirebaseListAdapter<Store>(this, Store.class,
                android.R.layout.simple_list_item_1, storesReference) {

            // Populate view as needed
            @Override
            protected void populateView(View view, Store store, int position) {

                ((TextView) view.findViewById(android.R.id.list)).setText(store.getName());


            }
        });
    }
}