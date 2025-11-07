<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# A09:2025 로깅 및 알림 실패 (Logging & Alerting Failures) ![icon](../../assets/TOP_10_Icons_Final_Security_Logging_and_Monitoring_Failures.png){: style="height:80px;width:80px" align="right"}


## 배경 (Background). 

로깅 및 알림 실패는 #9 위치를 유지합니다. 이 카테고리는 관련 로깅 이벤트에 대한 조치를 유도하는 데 필요한 알림 기능을 강조하기 위해 약간의 이름 변경이 있습니다. 이 카테고리는 항상 데이터에서 과소 대표될 것이며, 커뮤니티 설문조사 참가자들로부터 세 번째로 목록의 위치로 투표되었습니다. 이 카테고리는 테스트하기가 매우 어렵고 CVE/CVSS 데이터에서 최소한의 표현만 가지고 있습니다(723개의 CVE만). 그러나 가시성 및 사고 알림 및 포렌식에 매우 큰 영향을 줄 수 있습니다. 이 카테고리에는 *로그 파일에 대한 출력 인코딩을 적절하게 처리하는 문제 (CWE-117), 로그 파일에 민감한 데이터 삽입 (CWE-532), 불충분한 로깅 (CWE-778)*이 포함됩니다.


## 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>11.33%
   </td>
   <td>3.91%
   </td>
   <td>85.96%
   </td>
   <td>46.48%
   </td>
   <td>7.19
   </td>
   <td>2.65
   </td>
   <td>260,288
   </td>
   <td>723
   </td>
  </tr>
</table>



## 설명 (Description). 

로깅 및 모니터링 없이는 공격과 침해를 탐지할 수 없으며, 알림 없이는 보안 사고 중에 빠르고 효과적으로 대응하기가 매우 어렵습니다. 불충분한 로깅, 지속적인 모니터링, 탐지 및 활성 응답을 시작하는 알림은 다음 경우 발생합니다:


* 로그인, 실패한 로그인 및 고가치 거래와 같은 감사 가능한 이벤트가 로깅되지 않거나 일관되지 않게 로깅되는 경우(예: 성공적인 로그인만 로깅하고 실패한 시도는 로깅하지 않음).
* 경고 및 오류가 없거나 부적절하거나 불명확한 로그 메시지를 생성하는 경우.
* 로그의 무결성이 변조로부터 적절하게 보호되지 않는 경우.
* 애플리케이션 및 API의 로그가 의심스러운 활동에 대해 모니터링되지 않는 경우.
* 로그가 로컬에만 저장되고 적절하게 백업되지 않는 경우.
* 적절한 알림 임계값 및 응답 에스컬레이션 프로세스가 제자리에 있지 않거나 효과적이지 않은 경우. 알림이 합리적인 시간 내에 수신되거나 검토되지 않습니다.
* 동적 애플리케이션 보안 테스트(Dynamic Application Security Testing, DAST) 도구(예: Burp 또는 ZAP)에 의한 침투 테스트 및 스캔이 알림을 트리거하지 않는 경우.
* 애플리케이션이 실시간 또는 거의 실시간으로 활성 공격을 탐지, 에스컬레이션 또는 알림할 수 없는 경우.
* 로깅 및 알림 이벤트를 사용자나 공격자에게 보이게 하여 민감한 정보 누출에 취약한 경우(참조 [A01:2025-접근 제어 취약점 (Broken Access Control)](A01_2025-Broken_Access_Control.md)), 또는 로깅되어서는 안 되는 민감한 정보(예: PII 또는 PHI)를 로깅하는 경우.
* 로그 데이터가 올바르게 인코딩되지 않은 경우 로깅 또는 모니터링 시스템에 대한 인젝션 또는 공격에 취약한 경우.
* 애플리케이션이 오류 및 기타 예외 조건을 누락하거나 잘못 처리하여 시스템이 오류가 있었는지 인식하지 못하고 따라서 문제가 있었다는 것을 로깅할 수 없는 경우.
* 특수 상황을 인식하기 위한 알림 발행에 대한 적절한 '사용 사례'가 누락되었거나 오래된 경우.
* 너무 많은 거짓 양성 알림으로 인해 중요한 알림과 중요하지 않은 알림을 구별할 수 없어 너무 늦게 인식되거나 전혀 인식되지 않는 경우(SOC 팀의 물리적 과부하).
* 탐지된 알림이 사용 사례에 대한 플레이북이 불완전하거나 오래되었거나 누락되어 올바르게 처리할 수 없는 경우.


## 예방 방법 (How to prevent).

애플리케이션의 위험에 따라 개발자는 다음 제어 중 일부 또는 전부를 구현해야 합니다:


* 모든 로그인, 접근 제어 및 서버 측 입력 검증 실패가 의심스럽거나 악의적인 계정을 식별하기에 충분한 사용자 컨텍스트로 로깅되고 지연된 포렌식 분석을 허용할 만큼 충분한 시간 동안 보관되도록 하세요.
* 보안 제어를 포함하는 앱의 모든 부분이 성공하든 실패하든 로깅되도록 하세요.
* 로그 관리 솔루션이 쉽게 소비할 수 있는 형식으로 로그가 생성되도록 하세요.
* 로깅 또는 모니터링 시스템에 대한 인젝션 또는 공격을 방지하기 위해 로그 데이터가 올바르게 인코딩되도록 하세요.
* 모든 거래가 변조나 삭제를 방지하기 위한 무결성 제어가 있는 감사 추적을 가지도록 하세요. 예: 추가 전용 데이터베이스 테이블 또는 유사한 것.
* 오류를 발생시키는 모든 거래가 롤백되고 다시 시작되도록 하세요. 항상 닫힌 상태로 실패하세요.
* 애플리케이션이나 사용자가 의심스럽게 행동하면 알림을 발행하세요. 개발자에 대한 이 주제에 대한 가이드를 만들어 이에 대해 코딩하거나 이를 위한 시스템을 구매할 수 있도록 하세요.
* DevSecOps 및 보안 팀은 의심스러운 활동이 보안 운영 센터(Security Operations Center, SOC) 팀에 의해 빠르게 탐지되고 대응되도록 플레이북을 포함한 효과적인 모니터링 및 알림 사용 사례를 수립해야 합니다.
* 공격자에 대한 함정으로 애플리케이션에 '허니토큰(honeytokens)'을 추가하세요. 예: 데이터베이스, 데이터, 실제 및/또는 기술 사용자 신원으로. 정상적인 비즈니스에서 사용되지 않기 때문에 모든 액세스는 거의 거짓 양성 없이 알림을 받을 수 있는 로깅 데이터를 생성합니다.
* 행동 분석 및 AI 지원은 선택적으로 알림에 대한 낮은 거짓 양성 비율을 지원하는 추가 기술이 될 수 있습니다.
* 국가 표준 기술 연구소(National Institute of Standards and Technology, NIST) 800-61r2 이상과 같은 사고 대응 및 복구 계획을 수립하거나 채택하세요. 소프트웨어 개발자에게 애플리케이션 공격 및 사고가 어떻게 보이는지 가르쳐 보고할 수 있도록 하세요.

OWASP ModSecurity Core Rule Set과 같은 상용 및 오픈소스 애플리케이션 보호 제품과 Elasticsearch, Logstash, Kibana (ELK) 스택과 같은 오픈소스 로그 상관 소프트웨어가 이러한 문제를 해결하는 데 도움이 될 수 있는 사용자 정의 대시보드 및 알림 기능을 제공합니다. 거의 실시간으로 공격에 대응하거나 차단하는 데 도움이 될 수 있는 상용 관찰 가능성 도구도 있습니다.


## 공격 시나리오 예 (Example attack scenarios).

**시나리오 #1:** 어린이 건강 계획 제공자의 웹사이트 운영자는 모니터링 및 로깅 부족으로 인해 침해를 탐지할 수 없었습니다. 외부 당사자가 건강 계획 제공자에게 공격자가 350만 명 이상의 어린이의 수천 개의 민감한 건강 기록에 액세스하고 수정했다고 알렸습니다. 사고 후 검토에서 웹사이트 개발자가 중요한 취약점을 해결하지 않았음을 발견했습니다. 시스템에 대한 로깅이나 모니터링이 없었기 때문에 데이터 침해는 2013년부터 진행 중일 수 있었으며, 7년 이상의 기간이었습니다.

**시나리오 #2:** 주요 인도 항공사는 수백만 명의 승객의 10년 이상의 개인 데이터를 포함하는 데이터 침해를 겪었으며, 여기에는 여권 및 신용 카드 데이터가 포함되었습니다. 데이터 침해는 타사 클라우드 호스팅 제공자에서 발생했으며, 일정 시간 후 항공사에 침해를 알렸습니다.

**시나리오 #3:** 주요 유럽 항공사가 GDPR 보고 가능한 침해를 겪었습니다. 침해는 공격자가 40만 개 이상의 고객 결제 기록을 수집한 결제 애플리케이션 보안 취약점을 악용한 것으로 보고되었습니다. 결과적으로 항공사는 개인정보 보호 규제 기관에 의해 2천만 파운드의 벌금을 부과받았습니다.


## 참고 자료 (References). 

-   [OWASP 사전 대응 제어: C9: 로깅 및 모니터링 구현 (OWASP Proactive Controls: C9: Implement Logging and Monitoring)](https://top10proactive.owasp.org/archive/2024/the-top-10/c9-security-logging-and-monitoring/)

-   [OWASP 애플리케이션 보안 검증 표준: V16 보안 로깅 및 오류 처리 (OWASP Application Security Verification Standard: V16 Security Logging and Error Handling)](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md)

-   [OWASP 치트 시트: 애플리케이션 로깅 어휘 (OWASP Cheat Sheet: Application Logging Vocabulary)](https://cheatsheetseries.owasp.org/cheatsheets/Application_Logging_Vocabulary_Cheat_Sheet.html)

-   [OWASP 치트 시트: 로깅 (OWASP Cheat Sheet: Logging)](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

-   [데이터 무결성: 랜섬웨어 및 기타 파괴적 이벤트로부터 복구 (Data Integrity: Recovering from Ransomware and Other Destructive Events)](https://csrc.nist.gov/publications/detail/sp/1800-11/final)

-   [데이터 무결성: 랜섬웨어 및 기타 파괴적 이벤트에 대한 자산 식별 및 보호 (Data Integrity: Identifying and Protecting Assets Against Ransomware and Other Destructive Events)](https://csrc.nist.gov/publications/detail/sp/1800-25/final)

-   [데이터 무결성: 랜섬웨어 및 기타 파괴적 이벤트 탐지 및 대응 (Data Integrity: Detecting and Responding to Ransomware and Other Destructive Events)](https://csrc.nist.gov/publications/detail/sp/1800-26/final)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-117 로그에 대한 부적절한 출력 중화 (Improper Output Neutralization for Logs)](https://cwe.mitre.org/data/definitions/117.html)

* [CWE-221 누락된 정보 손실 (Information Loss of Omission)](https://cwe.mitre.org/data/definitions/221.html)

* [CWE-223 보안 관련 정보 누락 (Omission of Security-relevant Information)](https://cwe.mitre.org/data/definitions/223.html)

* [CWE-532 로그 파일에 민감한 정보 삽입 (Insertion of Sensitive Information into Log File)](https://cwe.mitre.org/data/definitions/532.html)

* [CWE-778 불충분한 로깅 (Insufficient Logging)](https://cwe.mitre.org/data/definitions/778.html)
