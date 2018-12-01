import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StructualDirectiveComponent } from './structual-directive.component';

describe('StructualDirectiveComponent', () => {
  let component: StructualDirectiveComponent;
  let fixture: ComponentFixture<StructualDirectiveComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StructualDirectiveComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StructualDirectiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
