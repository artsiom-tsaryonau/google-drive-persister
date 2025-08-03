from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from google_services import get_sheets_service

router = APIRouter()


# POST /drive/spreadsheets: Create new empty spreadsheet, with optional parent id
@router.post("/drive/spreadsheets")
async def create_spreadsheet(
    parent: Optional[str] = Query(None, description="Optional parent folder id"),
    title: str = Query(..., description="Spreadsheet title"),
    sheets_service=Depends(get_sheets_service),
):
    """
    Create a new empty spreadsheet with an optional parent folder.

    Example input request:
        POST /drive/spreadsheets?title=MySheet&parent=1xa0a3Z4YUfDZ3FQS4LrpdOZEkVp8hrq7

    Google API request sent:
        {
            "properties": {"title": "MySheet"},
            "parents": ["1xa0a3Z4YUfDZ3FQS4LrpdOZEkVp8hrq7"]
        }
        (POST to sheets_service.spreadsheets().create)
    """
    body = {"properties": {"title": title}}
    if parent:
        body["parents"] = [parent]
    try:
        spreadsheet = sheets_service.spreadsheets().create(body=body).execute()
        return spreadsheet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET /drive/spreadsheets/{spreadsheet_id}: Return a spreadsheet by id
@router.get("/drive/spreadsheets/{spreadsheet_id}")
async def get_spreadsheet(
    spreadsheet_id: str, sheets_service=Depends(get_sheets_service)
):
    """
    Get a spreadsheet by its ID.

    Example input request:
        GET /drive/spreadsheets/1R3rJWb50oW2JNOqKd4l0XlP-9hdMPr1c9cxjYX3PWnY

    Google API request sent:
        sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id)
    """
    try:
        spreadsheet = (
            sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        )
        return spreadsheet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# DELETE /drive/spreadsheets/{spreadsheet_id}: Delete a spreadsheet by id
@router.delete("/drive/spreadsheets/{spreadsheet_id}")
async def delete_spreadsheet(
    spreadsheet_id: str, sheets_service=Depends(get_sheets_service)
):
    """
    Delete a spreadsheet by its ID.

    Example input request:
        DELETE /drive/spreadsheets/1R3rJWb50oW2JNOqKd4l0XlP-9hdMPr1c9cxjYX3PWnY

    Google API request sent:
        sheets_service.spreadsheets().delete(spreadsheetId=spreadsheet_id)
    """
    try:
        sheets_service.spreadsheets().delete(spreadsheetId=spreadsheet_id).execute()
        return {"message": f"Spreadsheet {spreadsheet_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
