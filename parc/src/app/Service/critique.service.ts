import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CritiqueInterface } from '../Interface/critique.interface';

@Injectable({
  providedIn: 'root'
})
export class CritiqueService {
  constructor(private http: HttpClient) { }

  public postCritique(critique: CritiqueInterface): Observable<{message: string, result: number}> {
    return this.http.post<{message: string, result: number}>('/api/critique', critique);
  }

  public getCritiquesByAttractionId(attractionId: number): Observable<CritiqueInterface[]> {
    return this.http.get<CritiqueInterface[]>(`/api/critique/${attractionId}`);
  }
}