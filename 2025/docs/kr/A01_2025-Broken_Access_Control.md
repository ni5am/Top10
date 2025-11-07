<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

#  A01:2025 접근 제어 취약점 (Broken Access Control) ![icon](../../assets/TOP_10_Icons_Final_Broken_Access_Control.png){: style="height:80px;width:80px" align="right"}



## 배경 (Background). 

Top 10에서 #1 위치를 유지하며, 테스트된 애플리케이션의 100%가 어떤 형태의 접근 제어 취약점을 가지고 있는 것으로 발견되었습니다. 주목할 만한 CWE에는 *CWE-200: 무단 행위자에 대한 민감한 정보 노출 (Exposure of Sensitive Information to an Unauthorized Actor)*, *CWE-201: 전송된 데이터를 통한 민감한 정보 노출 (Exposure of Sensitive Information Through Sent Data)*, *CWE-918 서버 측 요청 위조 (Server-Side Request Forgery, SSRF)*, *CWE-352: 크로스 사이트 요청 위조 (Cross-Site Request Forgery, CSRF)*가 포함됩니다. 이 카테고리는 기여된 데이터에서 발생 횟수가 가장 많고, 관련 CVE 수가 두 번째로 많습니다.


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
   <td>40
   </td>
   <td>20.15%
   </td>
   <td>3.74%
   </td>
   <td>100.00%
   </td>
   <td>42.93%
   </td>
   <td>7.04
   </td>
   <td>3.84
   </td>
   <td>1,839,701
   </td>
   <td>32,654
   </td>
  </tr>
</table>



## 설명 (Description). 

접근 제어는 사용자가 의도한 권한 범위를 벗어나 행동할 수 없도록 정책을 강제합니다. 실패는 일반적으로 무단 정보 공개, 모든 데이터의 수정 또는 파괴, 또는 사용자 한계를 벗어난 비즈니스 기능 수행으로 이어집니다. 일반적인 접근 제어 취약점에는 다음이 포함됩니다:



* 최소 권한 원칙 위반, 일반적으로 기본적으로 거부(deny by default)로 알려져 있으며, 특정 기능, 역할 또는 사용자에 대해서만 액세스가 부여되어야 하지만 누구나 사용할 수 있는 경우.
* URL 수정(매개변수 조작 또는 강제 탐색), 내부 애플리케이션 상태, 또는 HTML 페이지를 수정하거나 API 요청을 수정하는 공격 도구를 사용하여 접근 제어 검사를 우회하는 경우.
* 고유 식별자를 제공하여 다른 사람의 계정 보기 또는 편집을 허용하는 경우(불안전한 직접 객체 참조, insecure direct object references).
* POST, PUT, DELETE에 대한 접근 제어가 누락된 접근 가능한 API.
* 권한 상승. 로그인하지 않고 사용자로 행동하거나 사용자로 로그인했을 때 관리자로 행동하는 경우.
* 메타데이터 조작, 예: JSON 웹 토큰(JSON Web Token, JWT) 접근 제어 토큰 재생 또는 조작, 권한 상승을 위해 조작된 쿠키 또는 숨겨진 필드, 또는 JWT 무효화 남용.
* CORS 설정 오류로 인해 무단 또는 신뢰할 수 없는 출처에서 API 액세스가 허용되는 경우.
* 강제 탐색(URL 추측)으로 인증되지 않은 사용자로 인증된 페이지에 또는 표준 사용자로 권한이 있는 페이지에 접근하는 경우.


## 예방 방법 (How to prevent). 

접근 제어는 공격자가 접근 제어 검사나 메타데이터를 수정할 수 없는 신뢰할 수 있는 서버 측 코드 또는 서버리스 API에서 구현될 때만 효과적입니다.



* 공개 리소스를 제외하고 기본적으로 거부하세요.
* 애플리케이션 전체에서 접근 제어 메커니즘을 한 번 구현하고 재사용하세요. 여기에는 크로스 오리진 리소스 공유(Cross-Origin Resource Sharing, CORS) 사용 최소화가 포함됩니다.
* 모델 접근 제어는 사용자가 모든 레코드를 생성, 읽기, 업데이트 또는 삭제할 수 있도록 허용하는 대신 레코드 소유권을 강제해야 합니다.
* 고유한 애플리케이션 비즈니스 제한 요구 사항은 도메인 모델에 의해 강제되어야 합니다.
* 웹 서버 디렉토리 목록을 비활성화하고 파일 메타데이터(예: .git) 및 백업 파일이 웹 루트 내에 없도록 하세요.
* 접근 제어 실패를 로깅하고 적절한 경우(예: 반복 실패) 관리자에게 알림을 보내세요.
* 자동화된 공격 도구의 피해를 최소화하기 위해 API 및 컨트롤러 접근에 속도 제한을 구현하세요.
* 상태 저장 세션 식별자는 로그아웃 후 서버에서 무효화되어야 합니다. 상태 비저장 JWT 토큰은 공격자의 기회 창을 최소화하기 위해 수명이 짧아야 합니다. 수명이 긴 JWT의 경우, OAuth 표준을 따라 액세스를 취소하는 것이 강력히 권장됩니다.
* 간단하고 선언적인 접근 제어를 제공하는 잘 확립된 도구 키트나 패턴을 사용하세요.

개발자와 QA 직원은 단위 및 통합 테스트에 기능적 접근 제어를 포함해야 합니다.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 애플리케이션이 계정 정보에 액세스하는 SQL 호출에서 검증되지 않은 데이터를 사용합니다:


```
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery( );
```


공격자는 단순히 브라우저의 'acct' 매개변수를 수정하여 원하는 계정 번호를 보낼 수 있습니다. 올바르게 검증되지 않으면 공격자는 모든 사용자의 계정에 액세스할 수 있습니다.


```
https://example.com/app/accountInfo?acct=notmyacct
```


**시나리오 #2:** 공격자는 단순히 브라우저가 URL을 대상으로 하도록 강제합니다. 관리자 페이지에 액세스하려면 관리자 권한이 필요합니다.


```
https://example.com/app/getappInfo
https://example.com/app/admin_getappInfo
```


인증되지 않은 사용자가 두 페이지 중 하나에 액세스할 수 있으면 결함입니다. 비관리자가 관리자 페이지에 액세스할 수 있으면 이것도 결함입니다.

**시나리오 #3:** 애플리케이션이 모든 접근 제어를 프론트엔드에 배치합니다. 공격자는 브라우저에서 실행되는 JavaScript 코드로 인해 `https://example.com/app/admin_getappInfo`에 도달할 수 없지만, 단순히 다음을 실행할 수 있습니다:


```
$ curl https://example.com/app/admin_getappInfo
```


명령줄에서.


## 참고 자료 (References). 

* [OWASP 사전 대응 제어: C1: 접근 제어 구현 (OWASP Proactive Controls: C1: Implement Access Control)](https://top10proactive.owasp.org/archive/2024/the-top-10/c1-accesscontrol/)
* [OWASP 애플리케이션 보안 검증 표준: V8 인증 (OWASP Application Security Verification Standard: V8 Authorization)](https://github.com/OWASP/ASVS/blob/master/5.0/en/0x17-V8-Authorization.md)
* [OWASP 테스트 가이드: 인증 테스트 (OWASP Testing Guide: Authorization Testing)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/README)
* [OWASP 치트 시트: 인증 (OWASP Cheat Sheet: Authorization)](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
* [PortSwigger: CORS 설정 오류 악용 (PortSwigger: Exploiting CORS misconfiguration)](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
* [OAuth: 액세스 취소 (OAuth: Revoking Access)](https://www.oauth.com/oauth2-servers/listing-authorizations/revoking-access/)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-22 제한된 디렉토리에 대한 경로명의 부적절한 제한 ('경로 순회', Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'))](https://cwe.mitre.org/data/definitions/22.html)

* [CWE-23 상대 경로 순회 (Relative Path Traversal)](https://cwe.mitre.org/data/definitions/23.html)

* [CWE-36 절대 경로 순회 (Absolute Path Traversal)](https://cwe.mitre.org/data/definitions/36.html)

* [CWE-59 파일 액세스 전 부적절한 링크 해석 ('링크 따르기', Improper Link Resolution Before File Access ('Link Following'))](https://cwe.mitre.org/data/definitions/59.html)

* [CWE-61 UNIX 심볼릭 링크 (심링크) 따르기 (UNIX Symbolic Link (Symlink) Following)](https://cwe.mitre.org/data/definitions/61.html)

* [CWE-65 Windows 하드 링크 (Windows Hard Link)](https://cwe.mitre.org/data/definitions/65.html)

* [CWE-200 무단 행위자에 대한 민감한 정보 노출 (Exposure of Sensitive Information to an Unauthorized Actor)](https://cwe.mitre.org/data/definitions/200.html)

* [CWE-201 전송된 데이터를 통한 민감한 정보 노출 (Exposure of Sensitive Information Through Sent Data)](https://cwe.mitre.org/data/definitions/201.html)

* [CWE-219 웹 루트 아래에 민감한 데이터가 있는 파일 저장 (Storage of File with Sensitive Data Under Web Root)](https://cwe.mitre.org/data/definitions/219.html)

* [CWE-276 잘못된 기본 권한 (Incorrect Default Permissions)](https://cwe.mitre.org/data/definitions/276.html)

* [CWE-281 권한의 부적절한 보존 (Improper Preservation of Permissions)](https://cwe.mitre.org/data/definitions/281.html)

* [CWE-282 부적절한 소유권 관리 (Improper Ownership Management)](https://cwe.mitre.org/data/definitions/282.html)

* [CWE-283 검증되지 않은 소유권 (Unverified Ownership)](https://cwe.mitre.org/data/definitions/283.html)

* [CWE-284 부적절한 접근 제어 (Improper Access Control)](https://cwe.mitre.org/data/definitions/284.html)

* [CWE-285 부적절한 인증 (Improper Authorization)](https://cwe.mitre.org/data/definitions/285.html)

* [CWE-352 크로스 사이트 요청 위조 (Cross-Site Request Forgery, CSRF)](https://cwe.mitre.org/data/definitions/352.html)

* [CWE-359 무단 행위자에 대한 개인 정보 노출 (Exposure of Private Personal Information to an Unauthorized Actor)](https://cwe.mitre.org/data/definitions/359.html)

* [CWE-377 불안전한 임시 파일 (Insecure Temporary File)](https://cwe.mitre.org/data/definitions/377.html)

* [CWE-379 불안전한 권한이 있는 디렉토리에 임시 파일 생성 (Creation of Temporary File in Directory with Insecure Permissions)](https://cwe.mitre.org/data/definitions/379.html)

* [CWE-402 새로운 영역으로 프라이빗 리소스 전송 ('리소스 누수', Transmission of Private Resources into a New Sphere ('Resource Leak'))](https://cwe.mitre.org/data/definitions/402.html)

* [CWE-424 대체 경로의 부적절한 보호 (Improper Protection of Alternate Path)](https://cwe.mitre.org/data/definitions/424.html)

* [CWE-425 직접 요청 ('강제 탐색', Direct Request ('Forced Browsing'))](https://cwe.mitre.org/data/definitions/425.html)

* [CWE-441 의도하지 않은 프록시 또는 중개자 ('혼란된 대리인', Unintended Proxy or Intermediary ('Confused Deputy'))](https://cwe.mitre.org/data/definitions/441.html)

* [CWE-497 무단 제어 영역에 대한 민감한 시스템 정보 노출 (Exposure of Sensitive System Information to an Unauthorized Control Sphere)](https://cwe.mitre.org/data/definitions/497.html)

* [CWE-538 외부에서 액세스 가능한 파일 또는 디렉토리에 민감한 정보 삽입 (Insertion of Sensitive Information into Externally-Accessible File or Directory)](https://cwe.mitre.org/data/definitions/538.html)

* [CWE-540 소스 코드에 민감한 정보 포함 (Inclusion of Sensitive Information in Source Code)](https://cwe.mitre.org/data/definitions/540.html)

* [CWE-548 디렉토리 목록을 통한 정보 노출 (Exposure of Information Through Directory Listing)](https://cwe.mitre.org/data/definitions/548.html)

* [CWE-552 외부 당사자가 액세스 가능한 파일 또는 디렉토리 (Files or Directories Accessible to External Parties)](https://cwe.mitre.org/data/definitions/552.html)

* [CWE-566 사용자 제어 SQL 기본 키를 통한 인증 우회 (Authorization Bypass Through User-Controlled SQL Primary Key)](https://cwe.mitre.org/data/definitions/566.html)

* [CWE-601 신뢰할 수 없는 사이트로의 URL 리디렉션 ('오픈 리디렉트', URL Redirection to Untrusted Site ('Open Redirect'))](https://cwe.mitre.org/data/definitions/601.html)

* [CWE-615 소스 코드 주석에 민감한 정보 포함 (Inclusion of Sensitive Information in Source Code Comments)](https://cwe.mitre.org/data/definitions/615.html)

* [CWE-639 사용자 제어 키를 통한 인증 우회 (Authorization Bypass Through User-Controlled Key)](https://cwe.mitre.org/data/definitions/639.html)

* [CWE-668 잘못된 영역에 리소스 노출 (Exposure of Resource to Wrong Sphere)](https://cwe.mitre.org/data/definitions/668.html)

* [CWE-732 중요한 리소스에 대한 잘못된 권한 할당 (Incorrect Permission Assignment for Critical Resource)](https://cwe.mitre.org/data/definitions/732.html)

* [CWE-749 노출된 위험한 메서드 또는 함수 (Exposed Dangerous Method or Function)](https://cwe.mitre.org/data/definitions/749.html)

* [CWE-862 누락된 인증 (Missing Authorization)](https://cwe.mitre.org/data/definitions/862.html)

* [CWE-863 잘못된 인증 (Incorrect Authorization)](https://cwe.mitre.org/data/definitions/863.html)

* [CWE-918 서버 측 요청 위조 (Server-Side Request Forgery, SSRF)](https://cwe.mitre.org/data/definitions/918.html)

* [CWE-922 민감한 정보의 불안전한 저장 (Insecure Storage of Sensitive Information)](https://cwe.mitre.org/data/definitions/922.html)

* [CWE-1275 부적절한 SameSite 속성을 가진 민감한 쿠키 (Sensitive Cookie with Improper SameSite Attribute)](https://cwe.mitre.org/data/definitions/1275.html)
