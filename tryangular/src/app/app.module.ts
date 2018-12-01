import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HelloComponent } from './components/hello/hello.component';
import { ComponentToViewComponent } from './components/component-to-view/component-to-view.component';
import { ViewToCompementComponent } from './components/view-to-compement/view-to-compement.component';
import { TwoWayBindingComponent } from './components/two-way-binding/two-way-binding.component';
import { StructualDirectiveComponent } from './components/structual-directive/structual-directive.component';

@NgModule({
  declarations: [
    AppComponent,
    HelloComponent,
    ComponentToViewComponent,
    ViewToCompementComponent,
    TwoWayBindingComponent,
    StructualDirectiveComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
